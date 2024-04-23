import yaml
import pandas as pd
import logging

# log 파일 쓰기
def log_writer(log_path, log_level, log_message):
    logging.basicConfig(filename=log_path, level=logging.INFO, format='[%(asctime)s][%(name)s][%(levelname)s] : %(message)s')
    logger = logging.getLogger()
    if log_level == 'DEBUG':
        logger.debug(log_message)
    elif log_level == 'INFO':
        logger.info(log_message)
    elif log_level == 'WARNING':
        logger.warning(log_message)
    elif log_level == 'ERROR':
        logger.error(log_message)
    elif log_level == 'CRITICAL':
        logger.critical(log_message)

# YAML 파일 읽기
def config_loader(config_path):
    this_config_path = config_path
    with open(this_config_path, 'r', newline='') as file:
        yaml_data = yaml.safe_load(file)
    return yaml_data

