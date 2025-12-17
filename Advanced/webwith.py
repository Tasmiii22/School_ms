import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


# driver=webdriver.Chrome()  #created browser instance

# driver.get("http://google.com")

# search=driver.find_element("name","q") #html attributes

# search.send_keys("netflix india")
# search.send_keys(Keys.RETURN)

# time.sleep(200)
# driver.quit()

#############################################################################

# driver=webdriver.Chrome()
# driver.get("https://www.flipkart.com/search?q=iphones")
# time.sleep(10)
# titles=driver.find_elements("css selector","div_4rR01T")
# for t in titles:
#     print(t.text)
# driver.quit() 


############################################################################

# driver=webdriver.Chrome()
# driver.get("https://www.flipkart.com/search?q=iphones")

# time.sleep(10)
# for i in range(5):
#     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(5)
# driver.quit()
# print("process done")    

###############################################################################

kiran=webdriver.Chrome()
kiran.get("https://books.toscrape.com/")
books=kiran.find_elements(By.CLASS_NAME,"product_pod")

with open("books.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    w.writerow(["Title","Price"])

    for b in books:
        t=b.find_element(By.TAG_NAME,"h3").text
        price=b.find_element(By.CLASS_NAME,"price_color").text
        w.writerow([t,price])
kiran.quit()
print("Done")        
