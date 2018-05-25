import pytasks


def runner(*args):
    if len(args) != 0:
        for i in args:
            getattr(pytasks, i)()
    else:
        getattr(pytasks, 'generate_numbers')()
        getattr(pytasks, 'count_characters')()
        getattr(pytasks, 'fizzbuzz')()
        getattr(pytasks, 'happy_numbers')()
        getattr(pytasks, 'is_palindrome')()
    return
