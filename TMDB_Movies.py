import pandas as pd
import numpy as np
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk import *


def recommend(movie):

    tmdb_5000_credits = pd.read_csv('tmdb_5000_credits.csv', delimiter=',')
    nRow, nCol = tmdb_5000_credits.shape

    tmdb_5000_movies = pd.read_csv('tmdb_5000_movies.csv', delimiter=',')
    nRow, nCol = tmdb_5000_movies.shape

    movies=tmdb_5000_movies.merge(tmdb_5000_credits,on="title")

    movies=movies[["movie_id","genres","title","overview","release_date","keywords","popularity","vote_average","cast","crew","production_companies"]]

    movies.dropna(inplace=True)

    def convert(obj):
        l=[]
        for i in ast.literal_eval(obj):
            l.append(i["name"])
        return l   

    movies["genres"]=movies["genres"].apply(convert)
    movies["keywords"]=movies["keywords"].apply(convert)
    movies["production_companies"]=movies["production_companies"].apply(convert)

    def convert3(obj):
        l=[]
        counter=0
        for i in ast.literal_eval(obj):
            if counter !=3:
                l.append(i["name"])
                counter+=1
            else:
                break
        return l  

    movies["cast"]=movies["cast"].apply(convert3)

    def director(obj): 
        l=[]
        for i in ast.literal_eval(obj):
            if i["job"]=="Director":
                l.append(i["name"])
                break
        return l 

    movies["crew"]=movies["crew"].apply(director)
    movies["overview"]=movies["overview"].apply(lambda x:x.split())

    #removing the space from all the columns values.
    movies["genres"]=movies["genres"].apply(lambda x:[i.replace(" ","") for i in x])
    movies["keywords"]=movies["keywords"].apply(lambda x:[i.replace(" ","") for i in x])
    movies["cast"]=movies["cast"].apply(lambda x:[i.replace(" ","") for i in x])
    movies["crew"]=movies["crew"].apply(lambda x:[i.replace(" ","") for i in x])

    movies["tags"]=movies["overview"]+movies["genres"]+movies["keywords"]+movies["cast"]+movies["crew"]

    new_df=movies[["movie_id","title","tags"]]

    #now we need to again convert tag col values into string 
    new_df["tags"]=new_df["tags"].apply(lambda x:" ".join(x))

    new_df["tags"]=new_df["tags"].apply(lambda x:x.lower())

    #use stemmer to create the root word
    from nltk.stem import WordNetLemmatizer

    wnl = WordNetLemmatizer()

    def x(text):
        y=[]
        for i in text.split():
            y.append(wnl.lemmatize(i)) 
        return " ".join(y) 

    new_df["tags"]=new_df["tags"].apply(x)

    cv=CountVectorizer(max_features=5000,stop_words="english")
    vector_tag=cv.fit_transform(new_df["tags"]).toarray()

    #calculate the cosine similarity one movie to another movie
    similarity=cosine_similarity(vector_tag)

    try: 
        movie_index= new_df[new_df['title']==movie].index[0]
        distance=similarity[movie_index]
        movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
        result = []
        for i in movie_list:
            result.append(new_df.iloc[i[0]].title)
        return result
    except:
        return []
        


if __name__ == "__main__":
    
    # lets see the recommendation
    movie = "Fight Club"
    recommendations = recommend(movie)
    for recommendation in recommendations:
        print(recommendation)