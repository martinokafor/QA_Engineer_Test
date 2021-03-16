import time
import pytest
import logging
from time import sleep
from selenium import webdriver
import nose
from selenium.webdriver.common.action_chains import ActionChains
from helium import *
from nose.plugins.multiprocess import MultiProcess
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
import os
class (TestClass):
    driver = webdriver.Chrome()
    driver.get("https://www.python.org/")
    driver.maximize_window()
    time.sleep(3)
    file_open = driver.find_element(By.XPATH, "//li[@class='tier-1 element-4   with-supernav']")
    file_open.click()
    time.sleep(4)
#file_open.screenshot("screen.png")
#file_open.click()
#driver.switch_to.window(driver.window_handles[1])
#set_driver(driver)
#click("Execute Login")
#attach_file("C:/Users/forem/OneDrive/Desktop/sample_project/ticket.pdf")
#file_open.send_keys("C:/Users/forem/OneDrive/Desktop/sample_project/ticket.pdf")
#file_open.send_keys("Enter")
driver.close()




time.sleep(5)
driver.quit()