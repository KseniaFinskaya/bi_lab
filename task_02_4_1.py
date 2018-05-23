""" Task "House Password":
Stephan and Sophia forget about security and use simple passwords for everything.
Help Nikola develop a password security check module.
The password will be considered strong enough if its length is greater than or equal to 10 symbols,
it has at least one digit, as well as containing one uppercase letter and one lowercase letter
in it. The password contains only ASCII latin letters or digits.
Input: A password as a string.
Output: Is the password safe or not as a boolean or any data type that can be converted and
processed as a boolean. In the results you will see the converted results."""


import re
password = str(input('Enter password: '))
rules = [re.match("[a-zA-Z0-9]+", password),
         10 <= len(password),
         ]
if all(rules):
    print('True')
else:
    print('False')
