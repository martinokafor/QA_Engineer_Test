import nose
from nose import with_setup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from helium import *
from time import sleep
import pytest
from web_element.web_element_reader import WebElementReader

dashboard_web_element = WebElementReader("dashboard_web.txt").web_element_reader()
#dashboard_web_element = dashboard_web_element.web_element_reader()

class Home:

    def __init__(self, driver, abstraction):
        self.driver = driver
        self.abstraction = abstraction
        # self.login = "login"
        # self.logout= "logout"

    def community(self):
        try:
            self.abstraction[1].wait_element_text(dashboard_web_element[1])
            click(dashboard_web_element[5])
        except (Exception) as exception:
            self.abstraction[0].logging_info("Community is not working")
            self.driver.save_screenshot(__name__ +".Dashboard.community.png")
            print(exception)
            assert False

    def python_logo(self):
        try:
            self.abstraction[1].wait_element_text(dashboard_web_element[1])
            click(dashboard_web_element[6])
        except (Exception) as exception:
            self.abstraction[0].logging_info("Python_logo is not working")
            self.driver.save_screenshot(__name__+ ".Dashboard.python_logo.png")
            print(exception)
            assert False

    def start_survey(self):
        try:
            self.abstraction[1].wait_element_text(dashboard_web_element[1])
            click(dashboard_web_element[7])
        except (Exception) as exception:
            self.abstraction[0].logging_info("Start survey is not working")
            self.driver.save_screenshot(__name__ +".Dashboard.start_survey.png")
            print(exception)
            assert False

@pytest.fixture
def home(driver, abstraction):
    home = Home(driver, abstraction)
    return home
#nosetests -v /c/Users/forem/OneDrive/Desktop/sample_project/test/*.py


