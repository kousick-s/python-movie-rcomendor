import operator
import collections
genresdict={}
count={}
avgsum={}
moviesdict={}
usersdict={}
ratingsdict={}
 


# Creating Movie Dict
with file("resources/movie.data") as f:
    content = [line.rstrip() for line in f]
    for x in content:
        x= x.split('|')
        moviesdict[x[0]]=x
        
# Creating Rating Dict 
with file("resources/ratings.data") as f:
    content = [line.rstrip() for line in f]
    i=1
    for x in content:
        x= x.split('\t')
        ratingsdict[i]=x;
        i=i+1
        
# Creating User Dict 
with file("resources/user.data") as f:
    content = [line.rstrip() for line in f]
    for x in content:
        x= x.split('|')
        usersdict[x[0]]=x;
        
# Creating Genres Dict 
with file("resources/genre.data") as f:
    content = [line.rstrip() for line in f]
    i=1
    for x in content:
        x= x.split('|')
        genresdict[x[0]]=x[1];
        

# Adding Average Rating
def average_Rating_Calculation():
    
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
    

#Getting Most Active User

def get_Most_Active_User():
    userwatchcount={}
    for x,y in ratingsdict.items():
        if y[0] in userwatchcount:
            countsum1=float(userwatchcount.get(y[0])) + 1
            userwatchcount[y[0]]=countsum1
        else:
            userwatchcount[y[0]]=1
    most_active_user=max(userwatchcount.iteritems(), key=operator.itemgetter(1))[0]
    print "Most Active User:",usersdict[most_active_user][0];
    
#Get Movie Id's for a particular year

def get_Top_Movie_By_Year(year):
    #average_Rating_Calculation()
    movieswithparticularyear={}
    with file("resources/movie.data") as f:
        moviecontent = [line.rstrip() for line in f]
        for x in moviecontent:
            y= x.split('|')
            z=y[2].split('-')
            if z[0] is not '':
                if z[2]==year:
                    keyval=y[0]
                    movieswithparticularyear[keyval]=float(avgsum.get(keyval)) 
    #print avgsum
    #movieswithparticularyear = collections.OrderedDict(sorted(d.items()))
    highest_rated_movie_by_year=max_of_dict(movieswithparticularyear)
    print "Top Movie By Year:", year + "-" + moviesdict[highest_rated_movie_by_year][1];
    
def get_Top_Movie_By_Genre(genre):
    
    moviesbyparticulargenre={}
    with file("resources/movie.data") as f:
        moviecontent = [line.rstrip() for line in f]
        genreindex=genresdict.get(genre)
        print genreindex
        for x in moviecontent:
            y= x.split('|')
            value=int(y[5+int(genreindex)])
            
            if value==1:
                
                moviesbyparticulargenre[y[0]]=float(avgsum[y[0]])
                
    highest_rated_movie_by_genre=max_of_dict(moviesbyparticulargenre)
    print "Top Movie By Genre:", genre + "-" + moviesdict[highest_rated_movie_by_genre][1];
    
def get_Top_Movie_By_YearAndGenre(year,genre):
    moviesbyparticulargenre={}
    movieswithparticularyear={}
    with file("resources/movie.data") as f:
        moviecontent = [line.rstrip() for line in f]
        genreindex=genresdict.get(genre)
        print genreindex
        for x in moviecontent:
            y= x.split('|')
            value=int(y[5+int(genreindex)])
            if value==1:
                moviesbyparticulargenre[y[0]]=y[2]
        for k,l in moviesbyparticulargenre.items():
            m=l.split('-')
            if m[0] is not '':
                if m[2]==year:
                    keyval=y[0]
                    movieswithparticularyear[k]=float(avgsum.get(k))      
    #highest_rated_movie_by_yearngenre=max(movieswithparticularyear.iteritems(), key=operator.itemgetter(1))[0]
    highest_rated_movie_by_yearngenre=max_of_dict(movieswithparticularyear)
    print "Top Movie By Year and Genre:", year + genre + "-" + moviesdict[highest_rated_movie_by_yearngenre][1];            

def get_Highest_Rated_Movie():
    average_Rating_Calculation()
    highest_rated_movie=max(avgsum.iteritems(), key=operator.itemgetter(1))[0]
    print "Highest Average Rated Movie:",moviesdict[highest_rated_movie][1];
def get_Most_Watched_Movie():
    average_Rating_Calculation()
    most_watched_movie=max(count.iteritems(), key=operator.itemgetter(1))[0]
    print "Most Watched Movie:",moviesdict[most_watched_movie][1];
    
def max_of_dict(sampledict):
    maxvalue=0
    maxkey='0'
    for m,n in sampledict.items():
        if n>=maxvalue:
            maxkey=m
    return maxkey
        
    
get_Highest_Rated_Movie()
get_Most_Watched_Movie()
get_Most_Active_User()
get_Top_Movie_By_Year('1996')
get_Top_Movie_By_Genre('Animation')
get_Top_Movie_By_YearAndGenre('1996','Animation')
#print movieswithparticularyear
