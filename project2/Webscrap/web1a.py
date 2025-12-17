import requests
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com"

response=requests.get(url)
 
if response.status_code==200:
  html=response.text


  soup=BeautifulSoup(html,"html.parser")

  quotes=soup.find_all("div","quote")

  for q in quotes:
    # print(q.get_text(strip=True))
    t=q.find("span",class_="text").get_text(strip=True)
    a=q.find("small",class_="author").get_text(strip=True)

    print(f"Author is {a} AND Text: {t}")
