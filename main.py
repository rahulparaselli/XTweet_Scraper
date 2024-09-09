from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pickle
from lxml import etree

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# set implicit wait time
driver.implicitly_wait(10)
driver.get("https://x.com")

# retrive cookies
savedCookies = pickle.load(open("cookies.pkl", "rb"))

# add cookies to the browser
for cookie in savedCookies:
    cookie['domain'] = ".x.com"
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(e)

# go to X.com
time.sleep(5)
driver.refresh()
time.sleep(10)

# search for tweets
driver.get("https://x.com/explore")
searchBox = driver.find_element(By.CLASS_NAME, "r-30o5oe")
searchBox.click()
searchBox.send_keys("#floods #India")
time.sleep(2)
searchBox.send_keys(Keys.RETURN)

"""soup = BeautifulSoup(driver.page_source, 'lxml')
pickle.dump(soup, open("tweets.pkl", "wb"))

#/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[1]/div/div/article
soup = pickle.load(open("tweets.pkl", "rb"))
soup = soup.find_all("div")
for div in soup:
    print(div.text)
    time.sleep(10)"""

# scroll down
articles_list = []
for i in range(10):
    artilces = driver.find_elements(By.TAG_NAME, "article")
    for article in artilces:
        articles_list.append(article.text)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

print(articles_list)