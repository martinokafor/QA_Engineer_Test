from helium import *
import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

from page_object.dashboard_page import dashboard
from page_object.home_page import home

def test_21(dashboard, home):
    dashboard.about()
    dashboard.getting_started()
    dashboard.search_field()
    home.community()
    home.python_logo()
    home.start_survey()



if __name__ == "__main__":
    pytest.main()