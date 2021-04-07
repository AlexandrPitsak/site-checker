from time import sleep
from lib.data_loader import get_config_data
from lib.site_checker import check_sites
import argparse


def main():
    config = get_config_data()
    interval = config['config']['interval_in_sec']
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=int, default=interval, help='Interval between checks')
    args = parser.parse_args()

    while True:
        check_sites()
        if args.i:
            sleep(args.i)
        else:
            sleep(interval)


if __name__ == "__main__":
    main()


