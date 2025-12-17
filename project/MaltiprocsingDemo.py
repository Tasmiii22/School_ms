import multiprocessing

def square(n):
  print(f"Squares of number is {n*n}")

if __name__=='__main__':
  p1=multiprocessing.Process(target=square,args=(5,))
  p2=multiprocessing.Process(target=square,args=(7,))

  p1.start()
  p2.start()

  p1.join()
  p2.join()

  print("All Done")