# import logging
#
# import pytest
# from helium import *
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# #python -m page_object.sample  ##### for executing package and avoiding relative import
#
# class Logg:
#     def logging_info(self, text):
#         self.FORMAT = '%(asctime)s %(levelname)s %(message)s' \
#                  ' %(lineno)d %(funcName)s %(filename)s'
#         logging.basicConfig(level=logging.INFO, format=self.FORMAT, filename="Testrun.log")
#
#         logging.info(text)
# #log10 = Logg()
# #log10.logging_info("About is not working")
# #log10.info("About is kaputt")
#
# @pytest.fixture()
# def loggi():
#     logg3 = Logg()
#     return logg3
#
#
# class WaitHelium:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def wait_element_text(self, element):
#         return wait_until(Text(element).exists, interval_secs=15)
#
#
# class WaitSelenium:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def wait_element(self, find_by, element):
#         return WebDriverWait(self.driver, 15).until(
#         EC.presence_of_element_located((find_by, element)))
#
# class CatchException:
#     pass
#
# @pytest.fixture
# def abstraction(driver):
#     logg2 = Logg()
#     #logg1.logging_info()
#     wait_helium = WaitHelium(driver)
#     wait_selenium = WaitSelenium(driver)
#     abstraction = [logg2, wait_helium, wait_selenium]
#     return abstraction
