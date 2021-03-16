import nose
from nose import with_setup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from helium import *
from time import sleep
import pytest
from selenium.common.exceptions import *
from web_element.web_element_reader import WebElementReader



dashboard_web_element = WebElementReader("dashboard_web.txt").web_element_reader()
#dashboard_web_element = dashboard_web_element.web_element_reader()

#########

class Dashboard:

    def __init__(self, driver, abstraction):
        self.driver = driver
        self.abstraction = abstraction
        # self.login = "login"
        # self.logout= "logout"

    def about(self):
        try:
            self.abstraction[2].wait_element(By.LINK_TEXT, dashboard_web_element[0])
            self.driver.find_element(By.LINK_TEXT, dashboard_web_element[0]).click()
        except (Exception, ElementNotVisibleException, TimeoutException, NoSuchElementException) as exception:
            self.abstraction[0].logging_info("Emeka is not working but making a mistake")
            self.driver.save_screenshot( __name__ + ".Dashboard.about.png")
            print(exception)
            assert False

    def getting_started(self):
        try:
            #sleep(3)
            #wait_until(Text(dashboard_web_element[1]).exists, interval_secs=30)
            self.abstraction[1].wait_element_text(dashboard_web_element[1])
            click(dashboard_web_element[1])
        except (Exception, ElementNotVisibleException) as exception:
            self.abstraction[0].logging_info("Getting Started is not working")
            self.driver.save_screenshot(__name__ + ".Dashboard.getting_started.png")
            print(exception)
            assert False

    def search_field(self):
        try:
            self.abstraction[1].wait_element_text(dashboard_web_element[3])
            write(dashboard_web_element[2], into=dashboard_web_element[3])
            self.abstraction[1].wait_element_text(dashboard_web_element[4])
            click(dashboard_web_element[4])
        except (Exception, ElementNotVisibleException) as exception:
            self.abstraction[0].logging_info("Search field is not working")
            self.driver.save_screenshot(__name__ + ".Dashboard.search_field.png")
            print(exception)
            assert False


@pytest.fixture
def dashboard(driver, abstraction):
    dashboard = Dashboard(driver, abstraction)
    return dashboard
#nosetests -v /c/Users/forem/OneDrive/Desktop/sample_project/test/*.py


