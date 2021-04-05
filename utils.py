def questionError(confirm):
    return not confirm.lower().startswith('y') and not confirm.lower().startswith('n')