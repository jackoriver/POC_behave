from loguru import logger

from features.utils.driver_config import driver_setup, driver_cleanup
from features.utils.log_config import start_logger


def before_all(context):
    # Initialize logger
    start_logger(context)
    context.logger = logger


def before_feature(context, feature):
    # Initialize Driver
    context.logger.info("Setting up the driver...")
    try:
        driver_setup(context)
    except Exception as e:
        context.logger.error(e)
        raise SystemExit
    # Navigate to the base page
    context.driver.get(context.config.userdata.get('app_url'))
    context.logger.info(f"Running feature: {feature.name}")


def after_feature(context, feature):
    driver_cleanup(context)
