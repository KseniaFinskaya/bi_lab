i = 0
while i < 101:
    i += 1
    rules = [(i % 3) == 0, (i % 5) == 0]
    if all(rules):
        print('Fizz Buzz')

    elif (i % 3) == 0:
        print('Fizz')

    elif (i % 5) == 0:
        print('Buzz')
    else:
        print(i)
