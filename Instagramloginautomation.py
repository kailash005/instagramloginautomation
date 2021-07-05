import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
username = input("Enter the username")
password = input("Enter the password")
input("Enter username and password and hit enter")
driver.get("https://www.instagram.com")
time.sleep(3) # time delay so that the page can load
#Entering the username
Username_box = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
Username_box.send_keys(username)
time.sleep(2)
#Entering the password
Password_box = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
Password_box.send_keys(password)
#Submitting the username and password
Password_box.send_keys(Keys.TAB)
Password_box.send_keys(Keys.ENTER)
time.sleep(10)
driver.close()
