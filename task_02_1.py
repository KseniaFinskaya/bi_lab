# Task "Finding palindrome": Write a program that check whether a string is palindrome or Not.


word = input('Enter word for palindrome check: ')
revword = word[:: -1]
if word == revword:
    print('True, ', revword, '.', sep='')
else:
    print('False, ', revword, '.', sep='')
