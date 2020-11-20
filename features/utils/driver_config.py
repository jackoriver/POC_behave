from selenium import webdriver


def driver_setup(context):
    """
    This function initialize and configures the driver
    :parameter
        context: object
    :returns
        nothing
    """
    if context.config.userdata.get('browser') in ['Chrome', 'chrome']:
        context.driver = webdriver.Chrome()
    elif context.config.userdata.get('browser') in ['Firefox', 'firefox']:
        context.driver = webdriver.Firefox()
    else:
        raise Exception('Browser entry is not properly setup in the behave config file.')

    try:
        context.driver.maximize_window()
    except Exception as e:
        context.logger.warning(f"Browser could not be maximized, setting the window size to 1920x1080. More info: {e}")
        context.driver.set_window_size(1920, 1080)

    context.driver.delete_all_cookies()
    context.driver.implicitly_wait(context.config.userdata.get('default_implicit_time'))
    context.driver.set_page_load_timeout(context.config.userdata.get('default_page_load_time'))
    context.logger.success('Driver created successfully!!')


def driver_cleanup(context):
    try:
        context.driver.quit()
        context.driver = None
        context.logger.debug("Closing browser...")
    except Exception as e:
        context.logger.error(e)
