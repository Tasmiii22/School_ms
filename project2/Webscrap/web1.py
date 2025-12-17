import requests
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com"

response=requests.get(url)
 
if response.status_code==200:
  html=response.text


  soup=BeautifulSoup(html,"html.parser")

  title=soup.find_all("span")

  for i in title:
    print(i.get_text(strip=True))

  # print("title",title.get_text(strip=True))
else:
  print("Failed to load page",response.status_code)

