#!/usr/bin/env python
import media
import os
import fresh_tomatoes

#List to hold movies in
movies=[]

#Read movies.txt, put into nested list
moviefile = [f.rstrip('\n') for f in open('movies.txt')] 
moviefile = [f.split(';') for f in moviefile]

#Create object instance for each movie, put in list.
movies.extend(media.Movie(f[0],f[1],f[2],f[3],f[4],f[5]) for f in moviefile)

#Pass movies to to be rendered in HTML
fresh_tomatoes.open_movies_page(movies)
