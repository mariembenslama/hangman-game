def response(confirm):
    return confirm.lower().startswith('y') or confirm.lower().startswith('n')

def agree(response):
    return response.lower().startswith('y')

def disagree(response):
    return response.lower().startswith('n')