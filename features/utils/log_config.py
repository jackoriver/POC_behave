import sys

from loguru import logger


def start_logger(context):
    logger.remove()
    logger.add(f"{context.config.userdata.get('file_name')}", format=f"{context.config.userdata.get('file_format')}",
               rotation=f"{context.config.userdata.get('retention_days')}", level=f"{context.config.userdata.get('file_level')}")
    logger.add(sys.stdout, colorize=True, format=f"{context.config.userdata.get('console_format')}",
               level=f"{context.config.userdata.get('console_log_level')}")
    logger.success("Logger initialized successfully!!")
