from enum import Enum
import itertools
from typing import Dict, List
from abc import ABC,abstractmethod
from dataclasses import dataclass

class  OrderStatus(Enum):
  PLACED="placed"
  CONFIRMED="confirmed"
  ONGOING="ongoing"
  OUT_FOR_DELIVERY="out_for_delivery"
  DELIVERED="delivered"
@dataclass # __init__,__repr__  automatic create
class Menuitem:
  id:int
  name:str
  price:float

class Restaurant:
  def __init__(self,name:str,restaurant_id:int):
    self.name=name
    self.id=restaurant_id
    self.items=Dict[int,Menuitem]={}
  def add_item(self,item:Menuitem):
    self.items[item._id]=item
  def list_items(self):
    return list(self._items.values())
  def __str__(self):
    return f"Restaurant({self._name})"



  
class User(ABC):
  def __init__(self,user_id:int,name:str):
    self._id=user_id
    self._name=name
  @abstractmethod
  def get_type(self):
    pass
  def __str__(self):
    return f"{self.get_type()} (id={self._id},name={self._name})"
  
class Customer(User):
    def get_type(self):
      return "Customer"
    def discount(self,amount:float):
      return amount
    
class PremiumCustomer(Customer):
  def get_type(self):
    return "PremiumCustomer"
  def discount(self,amount:float):
    return amount*0.10
  
class DeliveryPartner(User):
  def get_type(self):
    return "DeliveryPartner"

class Order:
  id:int
  customer:Customer
  restaurant:Restaurant
  items:List[Menuitem]
  total_price:float
  status:OrderStatus=OrderStatus.PLACED
  deliveryPartner:DeliveryPartner|None

  def update_status(self,new_status:OrderStatus):
    self.status=new_status
  def assign_partner(self,partner:DeliveryPartner):
    self.deliveryPartner=partner

class FoodRepo:
  def __init__(self):
    self._restaurants:Dict[int,Restaurant]={}
    self._customer:Dict[int,Customer]={}
    self._delivery_partner: Dict[int,DeliveryPartner]={}
    self._order:Dict[int,Order]={}

    self._item_counter=itertools(1)
    self._order_counter=itertools(1)
    self._user_counter=itertools(1)
    self._rest_counter=itertools(1)

  
  def add_resto(self,name:str):
    rid=next(self._rest_counter)
    rest=Restaurant(rid,name)
    self._restaurants[rid]=rest
    return rest
  
  def get_resto(self,rest_id:int):
    return self._restaurants[rest_id]
  
  def add_customer(self,name:str,premium:bool=False):
    cid=next(self._user_counter)
    if premium:
      customer=PremiumCustomer(cid,name)
    else:
      customer=Customer(cid,name)
    self._customer[cid]=customer
    return customer
  
  def add_delivery_partner(self,name:str):
    did=next(self._user_counter)
    dp=DeliveryPartner(did,name)
    self._delivery_partner[did]=dp
    return dp
  
  def list_delivery_partner(self):
    return list(self._delivery_partner.values())
  
  def add_item(self,restaurant:Restaurant,name:str,price:float):
    item=Menuitem(
      id=next(self._item_counter),
      name=name,
      price=price
      )
    restaurant.add_item(item)

  def save_order(self,order:Order):
    self._order[order.id]=order

  def get_order(self,order_id:int):
    return self._order[order_id]

class FoodDelivery:
    def __init__(self,repo:FoodRepo):
        self.repo=repo
    def place_order(self,customer_id:int,res_id:int,item_id:List[int]):
        customer=self.repo._customer[customer_id]
        restaurant=self.repo._Restaurants[res_id]

        items=[restaurant._item[i] for i in item_id]

        amount=sum(item.price for item in items)

        final_amount=customer.iscount(amount)

        order=Order(
            id=next(self.repo._order_counter),
            customer=customer,
            restaurant=restaurant,
            items=items,
            total_price=final_amount
        )


        self.repo.save_order(order)
        return order
    
    def assign_delivery_partner(self,order_id:int):
        order=self.repo.get_order(order_id)
        partners=self.repo.list_delivery_partner()
        if not partners:
            raise ValueError("No delivery partner avaialble")
        order.assign_partner(partners[0])


    def update_order_status(self,order_id:int,status:OrderStatus):
        order=self.repo.get_order(order_id)
        order.update_status(status)