import logging
logging.basicConfig(
  filename='app.log',
  level=logging.INFO,
  format='%(asctime)s-%(levelname)s-%(message)s',
  force=True

)

def login(Username):
  logging.info(f"User Login attemp:${Username}")
  if Username=="":
    logging.error("Cannot Provide empty username")
    return "Invalid Syntax"
  return "Login Successful"

print("TASMIYA SHIKALGAR")
print(" ")

  
