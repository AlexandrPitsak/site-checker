import requests

def check_availability(config, timeout=3):
    result = {}

    try:
        response = requests.get(config['url'], timeout=timeout)
        result['response'] = response

        if response.status_code >= 400:
            result['available'] = False
        else:
            result['available'] = True

        return result

    except requests.ConnectionError as ex:
        result['available'] = False
        result['error'] = str(ex)
        
        return result
