import behave_webdriver


def before_all(context):
    # Setup before test run
    context.behave_driver = behave_webdriver.Chrome()


def after_all(context):
    # Cleanup after tests run
    context.behave_driver.quit()
