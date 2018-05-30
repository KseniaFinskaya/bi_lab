import pandas as pd


df = pd.read_csv('IMDB-Movie-Data.csv', converters={
    'Rating': float})
grouped = df.groupby('Year')['Rating'].mean()
grouped.to_csv('ratings.csv', ['Year', 'Rating'])
