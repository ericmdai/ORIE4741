
# coding: utf-8

# In[21]:

import csv
import re

read = open("tmdb_5000_movies.csv")
#write = open("movies.csv")
reader = csv.reader(read)
#writer = csv.writer(write)


# In[22]:

count = 1
header = reader.next()
#header.extend(['genres1', 'genres2', 'genres3', 'keywords1', 'keywords2', 'keywords3', 'keywords4', 'keywords5', 'pc1', 'pc2', 'pc3'])
all = []
all.append(header)
for line in reader:
    genres = line[1]
    keywords = line[4]
    pc = line[9]
    release_date = line[11].split('-')
    g = re.findall('\d+', genres)
    k = re.findall('\d+', keywords)
    prod = re.findall('\d+', pc)
    line.append(release_date[0] if len(release_date) > 0 else '')
    line.append(release_date[1] if len(release_date) > 1 else '')
    line.append(g[0] if len(g) > 0 else '')
    line.append(g[1] if len(g) > 1 else '')
    line.append(g[2] if len(g) > 2 else '')
    line.append(k[0] if len(k) > 0 else '')
    line.append(k[1] if len(k) > 1 else '')
    line.append(k[2] if len(k) > 2 else '')
    line.append(prod[0] if len(prod) > 0 else '')
    line.append(prod[1] if len(prod) > 1 else '')
    line.append(prod[2] if len(prod) > 2 else '')
    all.append(line)

with open("movies.csv", 'w') as write:
    writer = csv.writer(write)
    writer.writerows(all)


# In[ ]:



