from loguru import logger

from features.utils.common_utils import connect_to_testlink, update_tc_result
from features.utils.driver_config import driver_setup, driver_cleanup
from features.utils.log_config import start_logger


def before_all(context):
    # Initialize logger
    start_logger(context)
    context.logger = logger

    # Setting Up Testlink
    context.project_name = context.config.userdata.get('project_name')
    context.plan_name = context.config.userdata.get('plan_name')
    context.platform_name = context.config.userdata.get('platform_name')
    context.build_name = context.config.userdata.get('build_name')
    try:
        connect_to_testlink(context)
        context.logger.success("Connection to Testlink successful!")
    except Exception as e:
        context.logger.debug(f"failed to connect to Testlink: {e}")


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


def after_scenario(context, scenario):
    # updating Testlink result
    try:
        update_tc_result(context, scenario.name, scenario.status.name.lower())
        context.logger.debug(f"Result for {scenario.name} updated in Testlink.")
    except Exception as e:
        context.logger.debug(f"Failed to update TC in Testlink: {e}")


def after_feature(context, feature):
    driver_cleanup(context)
