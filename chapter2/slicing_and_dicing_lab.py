import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('data/ml-1m/users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('data/ml-1m/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('data/ml-1m/movies.dat', sep='::', header=None, names=mnames)


data = pd.merge(pd.merge(ratings, users), movies)
mean_ratings = data.pivot_table('rating', rows='title', cols='gender', aggfuc='mean')
print 0
