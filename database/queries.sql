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



SELECT
title,
popularity,
overview
FROM movie
ORDER BY revenue DESC;


CREATE TABLE crew (
  movie_id int DEFAULT NULL,
  person_id int DEFAULT NULL,
  department_id int DEFAULT NULL,
  job varchar DEFAULT NULL
);


DROP TABLE IF EXISTS department;
CREATE TABLE department (
  department_id int(10) NOT NULL AUTO_INCREMENT,
  department_name varchar(200) DEFAULT NULL,
  PRIMARY KEY (department_id)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;


Select * from department

DROP TABLE IF EXISTS gender;
CREATE TABLE gender (
  gender_id int NOT NULL,
  gender varchar DEFAULT NULL,
  PRIMARY KEY (gender_id)
);

Select * from gender


-- Joining department and movie tables
SELECT department.department_id,
     department.department_name,
     movie.cast
FROM department
INNER JOIN department_name
ON department.department_id = department.department_name;


(All tables are available on database folder)