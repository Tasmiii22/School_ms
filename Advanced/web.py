# web scrapping  - dowload the code of website using python (html) and fetch required data 
#example
#  amazon  - price
# news headlines
#  weather data
#  quotes / jokes / facts

# Liabary
# 1) request
# 2) Beautifulsoup

import requests

from bs4 import BeautifulSoup
# url="https://in.puma.com"
# response=requests.get(url)

# if response.status_code==200:
#     html=response.text

#     soup=BeautifulSoup(html,"html.parser")

#     title=soup.find("p")

#     # print("title",title.get_text(strip=True))

# else:
#     print("Failed to load page!",response.status_code)

###############################################################################
# with Loop 

# url="https://in.puma.com"
# response=requests.get(url)
# if response.status_code==200:
#     html=response.text
#     soup=BeautifulSoup(html,"html.parser")
#     title=soup.find_all("h1  ")
#     for i in title:
#         print(i.get_text(strip=True))

# else:
#     print("Failed to load page!",response.status_code)

##############################################################################     

# url="https://quotes.toscrape.com"
# response=requests.get(url)
# if response.status_code==200:
#     S1=BeautifulSoup(response.text,"html.parser")
#     quotes=S1.find_all("div",class_="quote")
#     for q in quotes:
#         a=q.find('span',class_="text").get_text(strip=True)
#         b=q.find("small",class_="author").get_text(strip=True)

#         print(f'author is {b} and text is {a}')









url="http://www.meesho.in/"
response=requests.get(url)
if response.status_code==200:
    html=response.text
    soup=BeautifulSoup(html,"html.parser")
    title=soup.find_all("h1")
    for i in title:
        print(i.get_text(strip=True))

else:
    print("Failed to load page!",response.status_code)