import json
from os import path


def generate_json_report(site_data):
    result_file = "latest_report.json"
    site_data_key = site_data['url']
    all_results = {}

    if path.exists(result_file):
        with open(result_file, 'r') as file:
            all_results = json.load(file)
            all_results[site_data_key] = site_data

        with open(result_file, "w") as file: 
            file.write(json.dumps(all_results, indent=4))
    else:
        with open(result_file, "w") as file: 
            all_results[site_data_key] = site_data
            file.write(json.dumps(all_results, indent=4))
