import logging


# 1
def division_num(num1, num2):
    if num2 == 0:
        raise Exception('DevisionError: devision by zero is forbidden!')
    print(num1 / num2)


division_num(5, 0)


# 2
def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError as err_obj:
        print(logging.exception(err_obj))


print_list_element([0, 1, 2, 3, 4], 5)


# 3
def add_to_list_in_dict(thedict, listname, element):
    try:
        thedict[listname]
    except KeyError:
        thedict[listname] = []
        print('Created %s.' % listname)

    else:
        print('Added %s to %s.' % (element, listname))

    finally:
        thedict[listname].append(element)
        print('%s already has %d elements.' % (listname,
                                               len(thedict[listname])))


tlist = {'a': [10, 20], "b": [50]}
add_to_list_in_dict(tlist, 'Hello', 5)
print(tlist)
print('======')
add_to_list_in_dict(tlist, 'Hello', 10)
print(tlist)
