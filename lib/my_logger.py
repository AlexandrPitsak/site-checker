import logging
from lib.data_loader import get_config_data



def logger(message, level = logging.INFO, console_log = True):
    config = get_config_data()
    log_name = config['config']['log_file_name']
    fmt = '%(levelname)s  %(asctime)s  \n%(message)s'
    formatter = logging.Formatter(fmt)

    logging.basicConfig(filename=log_name, filemode='a', format=fmt, level=logging.INFO)

    if console_log:
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)
        logging.getLogger("").addHandler(console)



    if (level == logging.INFO):
        logging.info(message)

    if (level == logging.ERROR):
        logging.error(message)

    if (level == logging.CRITICAL):
        logging.critical(message)

    logging.getLogger("").removeHandler(console)

