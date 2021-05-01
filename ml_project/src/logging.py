import logging
import logging.config
import yaml

LOGGING_CONFIG_FILE = "configs/logging.conf.yaml"
APPLICATION_NAME = "train"

def setup_logging():
    """Setup loggers"""
    with open(LOGGING_CONFIG_FILE, 'r') as f:
        logging.config.dictConfig(yaml.safe_load(f))

setup_logging()

logger = logging.getLogger(APPLICATION_NAME)
