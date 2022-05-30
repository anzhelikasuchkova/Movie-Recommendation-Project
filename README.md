## TMDB_5000_Movies_Recommendation_System
### Overview
This is a movie recommendation system that uses different machine learning and data science methods like tf-idf and cosine similarity to recommend movies based on a criterion or a movie. 

### Requisites
- pandas
- numpy
- matplotlib
- scikitlearn

### Results
- We define a function that takes in a movie title as an input and outputs a list of the 10 most similar movies. Firstly, for this, we need a reverse mapping of movie titles and DataFrame indices. In other words, we need a mechanism to identify the index of a movie in our metadata DataFrame, given its title.


![Screen Shot 2022-05-29 at 11 25 52 PM](https://user-images.githubusercontent.com/95242493/170922642-7099bb00-6e57-4fee-b073-158c01127d87.png)





- While the recommending system produces good results now, It's scope is limited. Since most non franchise movies may not match based on words used in overview. Like in our example above interstellar gave us mostly accurate recommendations but Stuart Little has no real association to interstellar. So we will also use the other metadata available to us like director, actors, genres along with the keywords from the plot description. The results show some improvements as following:

![Screen Shot 2022-05-29 at 11 26 35 PM](https://user-images.githubusercontent.com/95242493/170922722-79809ae4-9152-4337-9bda-e86f18328320.png)

=======
## Technologies Used:

- Jupyter Notebook 
- Pandas
- Supervised Machine Learning: sklearn
- PostgreSQL
- Heroku
- VScode
- Python
- HTML/CSS
- JSON
- Quickdatabasediagram.com
- Google Slides

## Content:

The team members have drafted their project, including the following:
- Selected topic: **Movie Recommendation System**
- Reason we selected the topic: **Sometimes it can be time consuming to find a movie to watch that you will enjoy, this will look at a movie you have liked or watched and suggest movies that you may like based on your preferences**
- Description of the source of data:

**[Source: TMDB](https://www.themoviedb.org/)**

<img width="1345" alt="Screen Shot 2022-05-19 at 11 46 36 PM" src="https://user-images.githubusercontent.com/93845867/169668204-9a8d84b8-77a3-414d-ae86-6bb128ec7bbe.png">



## Questions we hope to answer with the data:
  - **What data would work best for this analysis?**
  - **What type of machine learning model would work best?**
  - **Can we make predictions based on keywords?**
  - **What kind of input do we need from the user?**

## Diagram of the Relational Data Model:

<img width="612" alt="Screen Shot 2022-05-21 at 1 35 51 PM" src="https://user-images.githubusercontent.com/93845867/169668225-4fee8c86-3a1e-4a03-8d2a-7145c27508e4.png">

## Slideshow:

https://docs.google.com/presentation/d/1HeAANIuZ8QjEb9GCQByyh6V3iVE2rak_viHoUIHOROc/edit?usp=sharing

