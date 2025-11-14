def order_summary(item,quantity=3,*additional,**billdetails):
  print(item)
  print(quantity)
  print(additional)
  print(billdetails)
 
order_summary("MacEgg Burger",3,"coke,fries",menu="done")