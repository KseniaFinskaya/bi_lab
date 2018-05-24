import re
password = str(input('Enter password: '))
rules = [re.match("[a-zA-Z0-9]+", password),
         10 <= len(password),
         ]
if all(rules):
    print('True')
else:
    print('False')
