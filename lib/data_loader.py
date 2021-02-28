from lib.my_parser import yaml_parser

def get_config_data():
    data = yaml_parser('config.yaml')

    return data

def get_rules_data():
    config_data = get_config_data()
    rule_data = config_data['config']['rules_path']
    data = yaml_parser(rule_data)

    return data
