# db1=connectDatabase()



# singletone pattern - we want only one instace

# class Database:
#     _instance=None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance=super().__new__(cls)
#             print("Database Connected")
#         return cls._instance
#     def getConnection(self):

################################################################################

# import sqlite3


# conn=sqlite3.connect("prashant.sqlite")
# cur=conn.cursor()

# cur.execute("CREATE TABLE IF NOT EXISTS students (name String)")
# # cur.execute("INSERT INTO students(name) VALUES(?)",("MANOJ",))
# # cur.execute("INSERT INTO students(name) VALUES(?)",("AAdi",))
# cur.execute("INSERT INTO students(name) VALUES(?)",("Sk",))
# conn.commit()

# print("Done. Data add successfully")
            

##################################################################################

# class CreditCard:
#     def pay(self,amount):
#         print(f"Paid Rs.{amount} via credit card ")

# class Paypal:
#     def pay(self,amount):
#         print(f"Paid Rs.{amount} via Paypal ") 

# class UPI:
#     def pay(self,amount):
#          print(f"Paid Rs.{amount} via UPI ") 

# class paymentFactory:
#     def get_payment(self,method):
#         if method=="Card":
#             return CreditCard()
#         elif method=="paypal":
#                 return Paypal()
#         elif method=="UPI":
#              return UPI()
#         else:
#              return "CAsh Payment only"

# fac=paymentFactory()

# payment=fac.get_payment("Card")
# payment.pay(600)

# payusingpaypal=fac.get_payment("paypal")
# payusingpaypal.pay(1000)
#####################################################################################
# 2 Dec 2025

# Observer - Auto Notification

# class Youtuber:
#     def __init__(self,name,Rank):
#         self.name=name
#         self.Rank=Rank
#         self.subscribers=[]
#     def subscribe(self,subscriber):
#         self.subscribers.append(subscriber)
   

#     def upload_video(self,video):
#         print (f"\n {self.name} uploaded {video}")
#         for sub in self.subscribers:
#             sub.notification(self.name,video)
#   trial
# class Viewers:
#     def __init__(self,viewer):
#         self.viewer=viewer


# class Subscriber:
#     def __init__(self,name):
#         self.name=name
#     def notification(self,channel,video):
#         print(f"{self.name} got notification : {video} the chnnel name is {channel} and the video viewers is 1 M ")

# scout=Youtuber("Shreeman legend",1)

# sub1=Subscriber("Aadi")

# scout.subscribe(sub1)
 
# scout.upload_video("New Gaming Video")

###########################################################################

# Thread.py

import time 
import threading

def tea():
    print("tea is preparing")
    time.sleep(2)
    print("tea is now ready")

def createIdli():
    print ("Idli batter is preparing just") 
    time.sleep(3)
    print("Idli is ready to Eat")

def Poha():
    print("Poha is now preparing")
    time.sleep(4)
    print("Poha is ready")    

# print("------------------------without threading-----------------------")

# start=time.time()
# tea()
# createIdli()
# Poha()

# print(f"total time:{time.time()-start:} seconds")
# print()
                    
print("---------------with threading-------------------------")

start=time.time()
thread1=threading.Thread(target=tea)
thread2=threading.Thread(target=createIdli)
thread3=threading.Thread(target=Poha)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print(f"total time:{time.time()-start:2f} seconds")





        