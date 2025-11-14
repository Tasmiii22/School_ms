def order_summary(item,quantity=3,*additional,**billdetails):
  i=item
  q=quantity
  add=additional
  bill=billdetails
  return i,q,add,bill
print(order_summary("MacEgg Burger",3,"coke,fries",menu="done"))