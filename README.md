# TMDB 5000 Movies Recommendation System

## Overview:

This is a movie recommendation system that uses different machine learning and data science methods like CountVectorizer and cosine similarity to recommend movies based on a movie entered. 

### Slideshow:

https://docs.google.com/presentation/d/1HeAANIuZ8QjEb9GCQByyh6V3iVE2rak_viHoUIHOROc/edit?usp=sharing


## Technologies Used:
- Jupyter Notebook 
- Pandas
- Numpy
- Matplotlib
- Supervised Machine Learning: scikitlearn
- PostgreSQL
- Heroku
- VScode
- Python
- HTML/CSS
- JSON
- Quickdatabasediagram.com
- Google Slides

## Content:
- Selected topic: **Movie Recommendation System**
- Reason we selected the topic: **Everyone loves movies. We all are in a way connected to each other via this amazing medium. Sometimes it can be time consuming to find a movie to watch that you will enjoy. How often do you find yourself scrolling through multiple apps looking for something that will scratch that itch but also isn't something you've already watched a million times.**
- What does the model do? **Our model looks at a movie you already like and suggests movies that you may like based on your preferences. The working principle is very simple. We first check if the movie name input is in the database and if it is we use our recommendation system to find similar movies and sort them based on their similarity distance and output only the top 5 movies.**

## Description of the source of data:

**[Source: TMDB](https://www.themoviedb.org/)**

<img width="1345" alt="Screen Shot 2022-05-19 at 11 46 36 PM" src="https://user-images.githubusercontent.com/93845867/169668204-9a8d84b8-77a3-414d-ae86-6bb128ec7bbe.png">


## Questions we hope to answer with the data:
  - **What data would work best for this analysis?**
  - **What type of machine learning model would work best?**
  - **How can we make the predictions more accurate?**
  - **What kind of input do we need from the user?**

## Data Processing Steps

- The CSV was imported into a pandas dataframe using Jupyter Notebook
- Merged 2 datasets into 1 based on 'title' or 'id' 
- Removed unnecessary data 
- Kept: 'movie_id','title','overview','genres','keywords','cast','crew'
- Dropped null rows from dataframe
- Converted columns to a string of values
- Added the string of values to the column named 'tags' 
- Created a new dataframe:'movie_id','title', 'tags'
- Using WordNetLemmatizer changes to the words to its root form, applied to our tags column
- Using CountVectorizer, omitted stop words 
- Create a vector tag which transforms to an array 
- Calculating cosine similarity to compare movies results to one another
- Building the movie recommendation function 
- Display the recommendations

## Diagram of the Relational Data Model:

<img width="612" alt="Screen Shot 2022-05-21 at 1 35 51 PM" src="https://user-images.githubusercontent.com/93845867/169668225-4fee8c86-3a1e-4a03-8d2a-7145c27508e4.png">

# WebApp

We created a user friendly Web App where one could simply input the movie title and receive 5 different movie title suggestions to choose from.  We used flask app as the local host and then connected to Heroku to hold our webapp on an interface. When you insert the title the machine is training the model and therefore takes a few seconds to produce results.  In the future we would mitigate this process.   


## Recommendation for future analysis:

- **[TMDB Website](https://www.themoviedb.org/)** provides us with an API that can be used to source more recent movies. In the future we hope to implement the API instead of the current CSV file that the recommendation system is always up to date. Additionally, we would like to make the movie titles clickable with descriptions and movie trailers.

## Conclusions
The Wep App is utilizing our first machine learning model.  As we were working on the web app were were continually working on additional machine learning models to come up with a more precise user experience.  


# Anything the team would have done differently:

## Machine Learning:

### Results
- We define a function that takes in a movie title as an input and outputs a list of the 10 most similar movies. Firstly, for this, we need a reverse mapping of movie titles and DataFrame indices. In other words, we need a mechanism to identify the index of a movie in our metadata DataFrame, given its title.

![Screen Shot 2022-06-02 at 12 01 23 AM](https://user-images.githubusercontent.com/95242493/171563240-e0fbe8e3-f646-4bad-b84b-aab13dc37a0a.png)




- While the recommending system produces good results now, It's scope is limited. Since most non franchise movies may not match based on words used in overview. Like in our example above interstellar gave us mostly accurate recommendations but Stuart Little has no real association to interstellar. So we will also use the other metadata available to us like director, actors, genres along with the keywords from the plot description. The results show some improvements as following:


![Screen Shot 2022-06-02 at 12 01 51 AM](https://user-images.githubusercontent.com/95242493/171563294-d5810e7e-8dc1-4a7f-aca2-ee664164c8e8.png)



