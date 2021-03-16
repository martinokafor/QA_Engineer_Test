import nose
from nose import with_setup
import time
import pytest
import unittest

from nose.tools import raises

from page_object.dashboard_page import dashboard
from page_object.home_page import home


from selenium import webdriver
import pytesseract
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from helium import *
#
# class Test (unittest.TestCase):
#     def test_03(self):
#         pass
#
#     def test_04(self):
#         pass
import pytest
import nose
from nose import with_setup
from page_object.dashboard_page import Dashboard
#from .conftest import *
#setupteardown = SetupTeardown()
#dashboard = Dashboard()



#@with_setup(setupteardown.setup_func, setupteardown.teardown_func)
def test_01(dashboard, home):
    dashboard.about()
    dashboard.getting_started()
    dashboard.search_field()
    home.community()
    home.python_logo()
    home.start_survey()Jesus8282


#test_01= with_setup(setup_func, teardown_func) (test_01)



    #driver = start_chrome('https://www.python.org', headless=True)
    #driver = start_chrome('https://www.python.org')
    #driver = webdriver.Firefox()
    #driver = webdriver.Chrome()
    #driver.get("https://www.python.org")
    #driver.maximize_window()
    #set_driver(driver)
    #Config.implicit_wait_secs = 20
    #click("About")
    #click(S("@About"))
    #sleep(3)
    #click("Help")
    #click(S("@Help"))
    #sleep(3)
    #click("Donate")
    #click(S(".donate-button"))
    #driver.find_element(By.ID, "edit-name").send_keys("hello")
    #driver.find_element(By.ID, "edit-pass").send_keys("man")
    #field = driver.find_element(By.ID, "edit-pass")
    #driver = webdriver.Chrome()

    #driver.save_screenshot('screenshot1.png')
    #click("log in")
    #click(Button(below="Enter the password that accompanies your username."))
    #sleep(3)
    #driver.close()


    ### headless
    #options = Options() # generic worked
    #options = webdriver.ChromeOptions() # worked
    #options = webdriver.FirefoxOptions() # worked
    #options.add_argument('--headless') # worked
    #options.add_argument('--disable-gpu') # worked
    #driver = webdriver.Firefox()
    #driver = webdriver.Edge("C:/Users/forem/AppData/Local/Programs/Python/Python38/msedgedriver.exe") # worked
    #driver = webdriver.Chrome(chrome_options=options)   # worked
    # driver = webdriver.Firefox(firefox_options=options)   # worked
    #driver = webdriver.Ie(ie_options=options)# worked
    #driver.get('https://www.python.org')
    #driver.maximize_window()
    #sleep(2)
    #driver.find_element_by_xpath("//li[@id='about']//a[contains(text(),'About')]").click() # worked
    #driver.close()

    ## action chain and tesserach
    # ac = ActionChains(driver)
    # #ac.move_to_element(elem).move_by_offset(86.5, 55.8).click().perform()
    # #ac.move_to_element(By.CSS_SELECTOR("body.python.about"))
    # ac.move_by_offset(74.58, 32).click().perform()
    # sleep(6)
    # ac.move_by_offset(135.95, 52.85).click().perform()
    # sleep(6)
    #driver.quit()
    # driver.get_screenshot_as_file("screenshot.png")
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    #
    # img_cv = cv2.imread("C:/Users/forem/OneDrive/Desktop/repo/open_weather_api/screenshot.png")
    # img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    # print(pytesseract.image_to_string(img_rgb).encode('utf8'))
    # print(pytesseract.image_to_boxes(img_rgb).encode('utf8'))
    # # driver.quit()
    # print("end of test...")
    # options = Options()
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    #
    # driver = webdriver.Chrome(chrome_options=options)
    # #driver = webdriver.Chrome()
    # driver.get("https://www.python.org/")
    # driver.maximize_window()
    # time.sleep(3)
    # driver.find_element_by_xpath("//li[@id='about']//a[contains(text(),'About')]").click()



if __name__ == "__main__":
    pytest.main()
#sample_01()