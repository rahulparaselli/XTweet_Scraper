from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pickle

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
searchBox = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input")
searchBox.click()
searchBox.send_keys("#floods #India")
time.sleep(2)
searchBox.send_keys(Keys.RETURN)

