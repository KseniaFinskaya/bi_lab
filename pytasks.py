# generate_numbers


def generate_numbers(number=20):
    print({i**2: i for i in range(1, number + 1)})


# count_characters


def count_characters(count_me_string='abcdefgabc'):
    dict_out = {}
    for char in list(count_me_string):
        dict_out[char] = count_me_string.count(char)
    print(dict_out)


# fizzbuzz


def fizzbuzz():
    my_list = []
    i = 0
    while i < 100:
        i += 1
        rules = [(i % 3) == 0, (i % 5) == 0]
        if all(rules):
            my_list.append('Fizz Buzz')

        elif (i % 3) == 0:
            my_list.append('Fizz')

        elif (i % 5) == 0:
            my_list.append('Buzz')
        else:
            my_list.append(i)
    print(my_list)


# happy_numbers

def happy_numbers(j=1000):
    def is_happy(n):
        my_list = []
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in my_list:
                return False
            my_list.append(n)
        return True
    happy_list = []
    for i in range(1, j + 1):
        if is_happy(i):
            happy_list.append(i)
    print(happy_list)


# is_palindrome


def is_palindrome(word='madam'):
    revword = word[:: -1]
    if word == revword:
        print('True')
    else:
        print('False')
