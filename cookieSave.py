from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pickle

def SaveCookies():
    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()

    # go to X.com
    driver.get("https://x.com/i/flow/login")
    # set implicit wait time
    driver.implicitly_wait(10)

    userName = "RahulR72595"
    password = "U#eF2M/KFb*Y/2n"

    # find the element that's name attribute is q (the google search box)
    userNameElement = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
    userNameElement.click()
    userNameElement.send_keys(userName)

    nextButton = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div")
    nextButton.click()

    passwordElement = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
    passwordElement.click()
    passwordElement.send_keys(password)

    loginButton = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button")
    loginButton.click()

    time.sleep(10)
    cookies = driver.get_cookies()
    """pickle.dump(cookies, open("cookies.pkl", "wb"))
    time.sleep(10)
    driver.close()"""
    return cookies

print(SaveCookies())
