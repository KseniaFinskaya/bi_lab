# task_02_1 "Finding palindrome"


word = input('Enter word for palindrome check: ')
revword = word[:: -1]
if word == revword:
    print('True, ', revword, '.', sep='')
else:
    print('False, ', revword, '.', sep='')
