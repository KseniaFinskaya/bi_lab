# 1


def generate_numbers(number=20):
    print({i**2: i for i in range(1, number+1)})


generate_numbers(20)

# 2


def count_characters(count_me_string):
    list_l = list(count_me_string)
    dict_out = {}
    for char in list(count_me_string):
        dict_out[char] = list_l.count(char)
    print(dict_out)


count_characters('abcdefgabc')
