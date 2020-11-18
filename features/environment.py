import sys
import time
from loguru import logger

from features.utils.driver_config import driver_setup


def before_all(context):
    logger.remove()
    logger.add("features/logs/file.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
    logger.add(sys.stdout, format="<green>{time:HH:mm:ss.SSS}</green> <level>| {level} | {message}</level>", colorize="True")
    context.logger = logger
    context.logger.info("Setting up the driver...")
    driver_setup(context)
    context.logger.info("Driver config ready!.")


def before_feature(context, feature):
    context.driver.get(context.config.userdata.get('app_url'))
    time.sleep(5)


def after_feature(context, feature):
    pass
