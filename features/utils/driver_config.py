from selenium import webdriver


def driver_setup(context):
    """
    This function initialize and configures the driver
    :parameter
        context: object
    :returns
        nothing
    """
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(context.config.userdata.get('default_implicit_time'))
    context.driver.set_page_load_timeout(context.config.userdata.get('default_page_load_time'))

    try:
        context.driver.maximize_window()
    except:
        context.driver.set_window_size(1920, 1080)
