from lib.site_data_collector import get_site_data
from lib.data_loader  import get_rules_data
from lib.reporters.log_reporter import generate_log_report
from lib.reporters.json_reporter import generate_json_report

def check_sites():
    data = get_rules_data()

    for config in data:
        site_data = get_site_data(config)
        generate_json_report(site_data)
        generate_log_report(site_data)