import logging
from lib.my_logger import logger


def log_beautifier(msg, result=''):
    indent = 30 - len(msg)
    if result == '':
        return " "*6 + msg + ' '*indent + f'\n'
    return " "*6 + msg + ' '*indent + f'[ {result} ]\n'
    

def generate_log_report(site_data):
    url = site_data['url']
    text = log_beautifier('URL', url)

    if 'error' in site_data:
        text += log_beautifier('PASS', False)
        error = site_data['error']
        text += log_beautifier('ERROR', error)

        return logger(text, level=logging.CRITICAL)
    else:
        status_code = site_data['response_status_code']
        response_time = site_data['response_time']
        text += log_beautifier('PASS', site_data['has_passed'])
        text += log_beautifier('Response Code', status_code)
        text += log_beautifier('Response Time', response_time)
        
        if len(site_data['rules']) > 0:
            text += log_beautifier('Rules:', '')
            for rule in site_data['rules']:
                _type = rule["rule"]
                value = rule["value"]
                result = 'PASS' if rule["result"] else 'FAIL'
                text += log_beautifier("     ({type}) {value}".format(type=_type, value=value, result=result), result)

        log_level = logging.INFO if site_data['has_passed'] else logging.ERROR

        return logger(text, log_level)








