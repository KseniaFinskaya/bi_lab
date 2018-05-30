import csv
import decimal
import itertools


with open('IMDB-Movie-Data.csv', 'r') as ifile, \
        open('top250_movies.csv', 'w') as ofile:
    reader = csv.DictReader(ifile)
    sortfile = sorted(reader, key=lambda x: decimal.Decimal(x['Rating']),
                      reverse=True)
    outputfile = csv.DictWriter(ofile, ['Title', 'Rating'],
                                extrasaction='ignore')
    outputfile.writeheader()
    for line in itertools.islice(sortfile, 1, 251):
        outputfile.writerow(line)
