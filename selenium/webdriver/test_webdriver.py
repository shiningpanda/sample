#-*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

class FirefoxTestCase(unittest.TestCase):
    
    def getdriver(self):
        return webdriver.Firefox()
    
    def test(self):
        '''Searches for the term `Cheese` on Google and then check the result page’s title.'''
        driver = self.getdriver()
        driver.get('http://www.google.com')
        inputElement = driver.find_element_by_name('q')
        inputElement.send_keys('Cheese!')
        inputElement.submit()
        try:
            WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith('cheese! -'))
        except TimeoutException:
            driver.quit()
            self.fail('failed to find page title')
        else:
            driver.quit()

class ChromeTestCase(FirefoxTestCase):
    
    def getdriver(self):
        return webdriver.Chrome()
         
if __name__ == '__main__':
    unittest.main()
