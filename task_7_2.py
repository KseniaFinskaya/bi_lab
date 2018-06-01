import argparse
import os.path
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument('--year', help='Display top250movies titles with year',
                    action='store_true')
parser.add_argument('--rate', action='store_true',
                    help='Display top250movies titles with rate')
parser.add_argument('--all', action='store_true',
                    help='shows title, rate, year')
parser.add_argument('--histogram', nargs='?',
                    help='Type year or rating. Displays histogram for rating '
                         'or for years')
parser.add_argument('--output_filename', action='store_true',
                    help='All data to specified filename file')
args = parser.parse_args()

imdb_csv = 'IMDB-Movie-Data.csv'
if os.path.exists(imdb_csv):
    df = pd.read_csv(imdb_csv)
    if args.year:
        sort_df = df.sort_values(['Rating'], ascending=False)
        sel_df = sort_df[['Title', 'Year']][:250]
        print(sel_df.to_string(index=False))
    if args.rate:
        sort_df = df.sort_values(['Rating'], ascending=False)
        sel_df = sort_df[['Title', 'Rating']][:250]
        print(sel_df.to_string(index=False))
    if args.all:
        sel_df = df[['Title', 'Rating', 'Year']]
        print(sel_df.to_string(index=False))
    if args.histogram == 'rating':
        grouped = df.groupby('Rating')['Rating'].count()
        ascgr = grouped.sort_index(ascending=False)
        print('Histogram for rating:')
        print(ascgr)
    if args.histogram == 'year':
        grouped = df.groupby('Year')['Year'].count()
        ascgr = grouped.sort_index(ascending=False)
        print('Histogram for year:')
        print(ascgr)
    if args.output_filename:
        df.to_csv(imdb_csv)
        print('File saved successfully!')
else:
    print('File doesn\'t exists! Download it first!')
