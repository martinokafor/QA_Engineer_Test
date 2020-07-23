# -*- coding: utf-8 -*-
"""Login with password of length less than eight"""

import time

from behave_webdriver.steps import *
from import_file import import_page_object
from import_file import import_configuration

page_object = import_page_object()
configuration = import_configuration()
"""Fct. calls for import_page_object and import_configuration"""

use_step_matcher("re")


@step("Enter Password of length less than eight")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    password = context.behave_driver.find_element_by_xpath(page_object[1])
    password.send_keys(configuration[3])


@then("Verify error message")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    time.sleep(1)
    error_message = context.behave_driver.find_element_by_xpath(page_object[4])
    error_message.is_displayed()
