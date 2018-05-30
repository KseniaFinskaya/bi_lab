import re


def set_password(password):
    rules = [re.match("[a-zA-Z0-9]+", password), 10 <= len(password)]
    if all(rules):
        return True
    else:
        return False
