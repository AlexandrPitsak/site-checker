
def check_one_of_rule(values, response_text):
    results = []
    result = {"rule": "one_of", "value": values, "result": False }

    for rule in values:
        
        if response_text.count(rule) >= 1:
            result['result'] = True
            results.append(result)

            return results
        
    results.append(result)

    return results       
