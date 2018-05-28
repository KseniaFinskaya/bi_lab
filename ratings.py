# read, group by year, mean, write

import pandas as pd


df = pd.read_csv('/Users/ksenia/IMDB-Movie-Data.csv', converters={'Rating': float})
grouped = df.groupby('Year')['Rating'].mean()
grouped.to_csv('/Users/ksenia/ratings.csv', ['Year', 'Rating'])
