from selenium import webdriver

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options = options, executable_path = r"C:\CDriver\chromedriver.exe")
driver.get("http://www.python.org")
driver.close() 