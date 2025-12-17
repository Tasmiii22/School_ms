import multiprocessing
import threading
import time

class count():
  c=0
  for i in range(50000000):
    c+=1
if __name__=='__main__':
   start=time.time()

   p1=multiprocessing.Process(target=count)
   p2=multiprocessing.Process(target=count)

   p1.start()
   p2.start()

   p1.join()
   p2.join()
print(f"time consumed,{time.time()-start:.2f}")