# open and read file

import os.path


def open_imdb(n=r'D:\Shared_VM\\IMDB-Movie-Data.csv'):
    if os.path.exists(n):
        with open(n, 'r+') as imdb:
            read_data = imdb.read()
    else:
        print('File doesn\'t exists')
    print(read_data)


open_imdb()
