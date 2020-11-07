from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Library for write 
import time



driver = webdriver.Chrome(executable_path=r"C:\CDriver\chromedriver.exe")
driver.get("https://www.facebook.com")

user = driver.find_element_by_id("email")
user.send_keys("2384013821")
time.sleep(3)


password = driver.find_element_by_id("pass")
password.send_keys("Alexix434010")
time.sleep(3)
password.send_keys(Keys.ENTER)

driver.close()

