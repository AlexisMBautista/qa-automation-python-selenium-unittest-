import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Library for write 
import time

class use_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\CDriver\chromedriver.exe")

    def testFind(self):
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("Google" , driver.title)

        search = driver.find_element_by_name("q")
        search.send_keys('Selenium')
        search.send_keys(Keys.ENTER)
        time.sleep(10)

        assert "No se encontro el elemento" not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()




        