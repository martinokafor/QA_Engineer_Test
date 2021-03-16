from selenium import webdriver
import pytesseract
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
import time
import pytest
import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from helium import *
from nose.plugins.multiprocess import MultiProcess
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pytest_addoption(parser):
    """Pytest command line options

        Args:
            parser(str): parses the command line option
    """
    parser.addoption(
        "--driver",
        action="store",
        default="chrome",
        help="my option: chrome or firefox")
    parser.addoption(
        "--headless",
        action="store",
        default="False",
        help="my option: False or True")


@pytest.fixture(scope="module")
def headless(request):
    return request.config.getoption("--headless")


#headless = headless()


@pytest.fixture(scope="module")
def driver(request, headless):
    """Driver option contain the webdriver test setup and teardown

        Args:
            request(fct)
        Returns:
            driver(fct): webdriver test setup and teardown
    """
    driver = request.config.getoption("--driver")
    if driver == "chrome":
        #headless = False
        if headless == "True":
            driver = start_chrome(headless=True)

        else:
            driver = start_chrome()
        driver.get("https://www.python.org/")
        #driver = webdriver.Chrome()
        #driver.get(config_file[0])
        # WebDriverWait(
        #     driver, 30).until(
        #     EC.title_contains("Address Book"))
        driver.maximize_window()
        time.sleep(3)
    elif driver == "firefox":
        #headless = True
        if headless == True:
            driver = start_firefox(headless=True)
        else:
            driver = start_firefox()
        driver.get("https://www.python.org/")
        #driver = webdriver.Firefox()less=Tru
        #driver.get(config_file[0])
        # WebDriverWait(
        #     driver, 30).until(
        #     EC.title_contains("Address Book"))
        driver.maximize_window()
        time.sleep(3)
    yield driver
    driver.close()
#
# FORMAT = '%(asctime)s %(levelname)s %(message)s' \
#                  ' %(lineno)d %(funcName)s %(filename)s'
# logging.basicConfig(level=logging.INFO, format=FORMAT, filename="Testrun.log")


class Logg:
    FORMAT = '%(asctime)s %(levelname)s %(message)s' \
             ' %(lineno)d %(funcName)s %(filename)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT, filename="Testrun.log")

    def logging_info(self, text):
        logger = logging.info(text)
        return logger


class WaitHelium:
    def __init__(self, driver):
        self.driver = driver

    def wait_element_text(self, element):
        return wait_until(Text(element).exists, interval_secs=15)


class WaitSelenium:
    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, find_by, element):
        return WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located((find_by, element)))

class CatchException:
    pass

@pytest.fixture
def abstraction(driver):
    logg2 = Logg()
    #logg1.logging_info()
    wait_helium = WaitHelium(driver)
    wait_selenium = WaitSelenium(driver)
    abstraction = [logg2, wait_helium, wait_selenium]
    return abstraction















# class SetupTeardown:
#     _multiprocess_shared_ = True
#     def __init__(self):
#         #self.driver = start_chrome(headless=True)
#         self.driver = start_chrome()
#
#     def setup_func(self):
#         self.driver.get("https://www.python.org/")
#         set_driver(self.driver)
#         self.driver.maximize_window()
#
#
#     def teardown_func(self):
#         self.driver.close()
#
# def begin():
#     print("It is working")