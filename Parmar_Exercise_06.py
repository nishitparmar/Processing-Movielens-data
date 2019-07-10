'''
Author: Nishit Parmar
CWID : 10432431
Exercise06

'''

#importing panda library
import pandas as pd 

usernames = ['user_id','gender','age','occupation','zip'] 

users = pd.read_table('users.dat', sep='::', header=None,names=usernames,engine = 'python')

ratingnames = ['user_id', 'movie_id', 'rating', 'timestamp'] 

ratings = pd.read_table('ratings.dat', sep='::', header=None, names=ratingnames,engine = 'python')

movienames = ['movie_id', 'title', 'genres'] 

movies = pd.read_table('movies.dat', sep='::', header=None,names=movienames,engine = 'python') 

print '\nThe first 3 rows of movies are:'

#To print the first 3 rows of movies

print movies[:3]

print '\nTher first 3 rows of users are:'

#To print the first 3 rows of users 

print users[:3]

print '\nThe first 3 rows of ratings are:'

#printing the first 3 rows of movies

print ratings[:3]

#Merge the three dataframes into a single dataframes

data = pd.merge(pd.merge(ratings, users), movies)

#the no. of records in movie.dat are printed 

print "\nThe no. of records in 'movies.dat' are:", len(movies.index) 

#the no. of records in users.dat are printed

print "\nThe no. of records in 'users.dat' are:", len(users.index) 

#the number of records in ratings.dat are printed

print "\nThe no. of records in 'ratings.dat' are:", len(ratings.index)

#printing the number of records

print "\nThe no. of records in 'data.dat' are:", len(data.index)

#Placing the numbers in occupations column with specific occupations permanentaly in the dataframe data

ocupation = ['0 other/not specified', '1 academic/educator','2 artist','3 clerical/admin','4 college/grad student',
'5 customer service','6 doctor/health care','7 executive/managerial','8 farmer','9 homemaker',
'10 K-12 student','11 lawyer','12 programmer','13 retired','14 sales/marketing','15 scientist',
'16 self-employed','17 technician/engineer','18 tradesman/craftsman','19 unemployed','20 writer']

for i in range(21):
    data['occupation'].replace(to_replace = i ,value = ocupation[i] ,inplace = True)

print "\nThe last three rows of the Dataframe data are:" 

#Printing the last three rows of Dataframe after replacement

print data[-3:] 

#Printing the five ocupations that give higher ratings for movies

print "\nThe five occupations that give higher ratings for movies are:"

print data.occupation.value_counts()[:5] 

