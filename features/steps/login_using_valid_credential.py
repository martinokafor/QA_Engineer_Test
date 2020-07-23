# -*- coding: utf-8 -*-
"""Verify login using valid credential"""

import time

from behave_webdriver.steps import *
from import_file import import_page_object
from import_file import import_configuration

page_object = import_page_object()
configuration = import_configuration()
"""Fct. calls for import_page_object and import_configuration"""

use_step_matcher("re")


@given("User on login page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.behave_driver.get(configuration[0])
    context.behave_driver.maximize_window()


@when("User enter Username")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    username = context.behave_driver.find_element_by_xpath(page_object[0])
    username.send_keys(configuration[1])


@step("Enter Password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    password = context.behave_driver.find_element_by_xpath(page_object[1])
    password.send_keys(configuration[2])


@step("Click Login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    time.sleep(1)
    login_button = context.behave_driver.find_element_by_xpath(page_object[2])
    login_button.is_enabled()
    login_button.click()


@then("User should be logged in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    time.sleep(1)
    successful_login_text = context.behave_driver.find_element_by_xpath(
        page_object[3])
    successful_login_text.is_displayed()
