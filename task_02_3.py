""" Task "FizzBuzz": Write a program that prints the numbers from 1 to 100,
but for multiples of three print “Fizz” instead of the number and for multiples of five print“Buzz”.
For numbers which are multiples of both three and five, print “FizzBuzz”."""

i = 0
while i < 101:
    i += 1
    rules = [(i % 3) == 0, (i % 5) == 0]
    if all(rules):
        print('Fizz Buzz')
        continue
    elif (i % 3) == 0:
        print('Fizz')
        continue
    elif (i % 5) == 0:
        print('Buzz')
    else:
        print(i)
