from lib.site_availability_checker import check_availability
from lib.rule_checkers.must_have_rule_checker import check_must_have_rule
from lib.rule_checkers.one_of_rule_checker import check_one_of_rule


def get_site_data(config):
    site_data = {
        'rules': [],
        "url": config['url']
    }

    availability_data = check_availability(config)

    if 'error' in availability_data:  # data for connection Error or invalid url
        site_data.update({
                'has_passed': False,
                'error': availability_data['error']
        })

        return site_data

    response = availability_data['response']  # response with code 200 or >= 400
    
    site_data.update({
        "response_time": str(response.elapsed),
        "response_status_code": response.status_code
    })

    if not availability_data['available']: 
        site_data.update({'has_passed': False})

        return site_data   

    if 'rules' in config:  

        for rule in config['rules']:

            if rule['rule'] == 'must_have': 
                site_data['rules'] += check_must_have_rule(rule['values'], response.text) 

            if rule['rule'] == 'one_of':
                site_data['rules'] += (check_one_of_rule(rule['values'], response.text))

    site_data['has_passed'] = True

    for rule in site_data['rules']:

        if not rule['result']:
            site_data['has_passed'] = False

    return site_data
