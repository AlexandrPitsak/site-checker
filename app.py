from time import sleep
from lib.data_loader import get_config_data
from lib.site_checker import check_sites


def main():
    config = get_config_data()
    interval = config['config']['interval_in_sec']

    while True:
        check_sites()
        sleep(interval)



if __name__ == "__main__":
    main()


