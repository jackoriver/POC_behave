from loguru import logger

from features.utils.driver_config import driver_setup, driver_cleanup
from features.utils.log_config import start_logger


def before_all(context):
    # Initialize logger
    start_logger(context)
    context.logger = logger

    # Initialize Driver
    context.logger.info("Setting up the driver...")
    try:
        driver_setup(context)
    except Exception as e:
        context.logger.error(e)
        raise SystemExit


def before_feature(context, feature):
    context.driver.get(context.config.userdata.get('app_url'))


def after_feature(context, feature):
    driver_cleanup(context)
