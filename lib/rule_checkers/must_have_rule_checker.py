
def check_must_have_rule(values, response_text):
    results = []

    for rule in values:
        result = {"rule": "must_have", "value": rule, "result": True }

        if response_text.count(rule) < 1:
            result['result'] = False

        results.append(result)

    return results
