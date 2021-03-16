import nose
from nose import with_setup
from page_object.dashboard_page import dashboard
from page_object.home_page import home
#from .conftest import *
import pytest
#dashboard = Dashboard()



#@with_setup(setupteardown.setup_func, setupteardown.teardown_func)
def test_012(dashboard, home):
    dashboard.about()
    dashboard.getting_started()
    dashboard.search_field()
    home.community()
    home.python_logo()
    home.start_survey()




if __name__ =="__main__":
    pytest.main()
