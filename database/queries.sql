queries.sql

# Creating the table movie

CREATE TABLE movie (
  budget int DEFAULT NULL,
  homepage varchar(1000) DEFAULT NULL,
  movie_id int NOT NULL,
  overview varchar(1000) DEFAULT NULL,
  popularity decimal(12,6) DEFAULT NULL,
  revenue bigint DEFAULT NULL,
  movie_status varchar(50) DEFAULT NULL,
  tagline varchar(1000) DEFAULT NULL,
  title varchar(1000) DEFAULT NULL,
  vote_average decimal(4,2) DEFAULT NULL,
  vote_count int DEFAULT NULL,
  PRIMARY KEY (movie_id)
);

select * from movie

# Creating a table to show movie budget, revenue and populatiry base on the movie table.

SELECT
title,
budget,
revenue,
vote_average
FROM movie
ORDER BY revenue DESC;

Drop table crew

CREATE TABLE crew (
  movie_id INT DEFAULT NULL,
  title_x VARCHAR DEFAULT NULL,
  cast_col VARCHAR,
  director VARCHAR,
  keywords VARCHAR,
  genres VARCHAR
);

select * from crew

'Create at least one joint'

-- Joining movie and crew tables
SELECT movie.movie_id,
     movie.title
FROM movie
INNER JOIN crew.id
	 crew.director,	 
ON movie.movie_id = crew.id;


Select movie.title, crew.cast_col, crew.director, crew.genres, movie.vote_average
from movie 
inner join crew on movie.movie_id = crew.movie_id

