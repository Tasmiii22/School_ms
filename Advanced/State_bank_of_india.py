import os
# class bank:


#   def customer_info(info,customer_id):
         
#          info.customer_id=customer_id
#          info.data_file = f"{customer_id}.txt"
#          if not os.path.exists(info.data_file):
#                with open(info.data_file, "w") as f:
#                 f.write("0")

              
# def deopsit(info,amount):
     
#      with open(info.data_file, "r") as f:
#          balance = float(f.read())
#          balance = amount
#      with open(info.data_file, "r") as f:
#          amount=int(input("enter a amount"))

balance=0
def deposit():
    global amount
    amount_self=int(input("enter amount"))          
    amount=balance+amount_self     
    print(f"{amount} deposit amount successfully")

def withdraw():
    global amount

    withdraw=int(input("enter amount:"))
    if withdraw>balance:
        print("insufficient balance")
        
    
 