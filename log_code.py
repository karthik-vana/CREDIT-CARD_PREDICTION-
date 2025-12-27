import logging


def setup_logging(script_name):
    logger = logging.getLogger(script_name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        # Create a file handler for the script
        handler = logging.FileHandler(f'C:\\Users\\Karthik\\Downloads\\ML_Main-Project\\Ml_pipeline\\logs\\{script_name}.log', mode='w')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False

    return logger