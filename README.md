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


![Screen Shot 2022-05-20 at 7 57 29 PM](https://user-images.githubusercontent.com/95242493/169630077-81989328-662c-43a5-9d28-c60b6924d654.png)



- While the recommending system produces good results now, It's scope is limited. Since most non franchise movies may not match based on words used in overview. Like in our example above interstellar gave us mostly accurate recommendations but Stuart Little has no real association to interstellar. So we will also use the other metadata available to us like director, actors, genres along with the keywords from the plot description. These can be taken from our dataset and added to the dataframes using the folowing code.


![Screen Shot 2022-05-20 at 7 57 56 PM](https://user-images.githubusercontent.com/95242493/169630097-271136de-7251-46b7-a940-9cef6ef66644.png)
