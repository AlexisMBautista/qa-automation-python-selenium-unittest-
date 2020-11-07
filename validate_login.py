from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Library for write 
import time



driver = webdriver.Chrome(executable_path=r"C:\CDriver\chromedriver.exe")
driver.get("http://localhost:3000/")

user = driver.find_element_by_id("email")
user.send_keys("a@paciente.com")
time.sleep(3)


password = driver.find_element_by_id("pass")
password.send_keys("Qwerty123")
time.sleep(3)
password.send_keys(Keys.ENTER)

driver.close()

