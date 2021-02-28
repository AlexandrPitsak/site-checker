import yaml
import glob  #finds all the pathnames matching a specified pattern 
from pathlib import Path 


def yaml_parser(path):
    file_list = glob.glob(f'{Path(__file__).parent}/../{path}') # get path from root dir of proj

    data = []

    if (len(file_list) == 1):
        return yaml.safe_load(open(file_list[0], 'r'))

    for file in file_list:
        data.append(yaml.safe_load(open(file, 'r')))

    return data


