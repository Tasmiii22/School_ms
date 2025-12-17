import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time


def save_data(data):
    db=pymysql.connect(
        host="localhost",
        user="root",
        password="1722",
        database="tasmiyaDB",
        charset="utf8mb4"
    )
    cur=db.cursor()
    query="""
    INSERT IGNORE INTO jobs(title,company,location,link)
    VALUES(%s,%s,%s,%s)
    """

    cur.executemany(query,data)
    db.commit()
    print("insert done", cur.rowcount)
    db.close()


def scrap_jobs():
    url="https://in.indeed.com/jobs?q=django+developer&l="

    d=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    d.get(url)

    time.sleep(5)

    soup=BeautifulSoup(d.page_source,'html.parser')
    d.quit()

    job_cards=soup.select("div.job_seen_beacon")

    scraped_data=[]
    for job in job_cards:
        title=job.select_one("h2.jobTitle span")
        title1=title.text.strip() if title else "N/A"

        find_company=job.select_one("span.companyName")
        if not find_company:
            find_company=job.select_one("div[class*='company'] span")
        company=find_company.text.strip() if find_company else "N/A"

        find_location = job.select_one("span.companyLocation")
        if not find_location:
            find_location = job.select_one("span.location")
        location = find_location.text.strip() if find_location else "N/A"

        link_tag=job.select_one("h2.jobTitle a")
        link="https://in.indeed.com"+link_tag["href"] if link_tag else ""

        scraped_data.append([title1,company,location,link])
    print("scraped data", len(scraped_data))

    save_data(scraped_data)
    print("Scraped data saved successfully")

if __name__=="__main__":
    scrap_jobs()

# create database jobDB;
# use JoDB;
# create table jobs(
# id int auto_increment primary key,
# title varchar(255),
# company varchar(255),
# location varchar(255),
# link TEXT,
# scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# UNIQUE(link(255))
# );