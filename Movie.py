import operator

# Creating Movie Dict
moviedict={}
with file("resources/movie.data") as f:
    content = [line.rstrip() for line in f]
    for x in content:
        x= x.split('|')
        moviedict[x[0]]=x
        
# Creating Rating Dict
ratingsdict={}  
with file("resources/ratings.data") as f:
    content = [line.rstrip() for line in f]
    i=1
    for x in content:
        x= x.split('\t')
        ratingsdict[i]=x;
        i=i+1
        
# Adding Average Rating
count={}
avgsum={}
for x,y in ratingsdict.items():
    if y[1] in count:
        countsum=float(count.get(y[1])) + 1
        count[y[1]]=countsum
        averagesum=float(avgsum.get(y[1])) + float(y[2]);
        avgsum[y[1]]=averagesum
    else:
        avgsum[y[1]]=y[2];
        count[y[1]]=1


for x,y in avgsum.items():
    total=float(y)
    avgsum[x]=total/float(count[x])
    
# Getting highest rated movie

highest_rated_movie=max(avgsum.iteritems(), key=lambda l: l[1])[0]
most_watched_movie=max(count.iteritems(), key=lambda l: l[1])[0]
print "Highest Average Rated Movie:",moviedict[highest_rated_movie][1];
print "Most Watched Movie:",moviedict[most_watched_movie][1];
