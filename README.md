

# Movie Ratings Database Project

This project is a movie ratings database management system implemented in Python using SQLAlchemy for database interactions, Alembic for migrations, and argparse for a command-line interface. It allows users to manage movies, their details, and user ratings.


# Getting Started

# The Repository:
   git clone: git@github.com:KevinKiseli/End_of_Phase_3_-Project.git

   then cd movie-ratings-database


- Install Dependencies:

pyenv install 3.8.13


- Initialize the Database:

python migrate.py


- Insert Sample Data:

python data_insert.py


# Usage:
# Command-Line Interface (CLI)
Use the provided command-line interface below to manage the movie database.

# List all movies
python cli.py --list-movies        

# Delete movie with ID 1
python cli.py --delete-movie 1    


# List ratings for user Kevin
python cli.py --list-user-ratings Kevin


# Interactive Script:
An interactive script is provided for users to input their movie ratings. Follow the below steps:

Run python interactive_script.py on terminal and follow the prompts to enter your username, movie details, and rating.


# Data Insertion:
The data_insert.py script demonstrates how to insert sample data which will be found in the .py file into the database.

Run python data_insert.py in the terminal and open movie_ratings.db to see your data.


# Database Migrations:
To apply database schema changes, use the migrate script.

This is dun by running python migrate.py


# Project Structure:
- alembic/: Contains Alembic migration scripts.

- database.py: Defines SQLAlchemy models and database setup.

- cli.py: Command-line interface for managing the movie database.

- data_insert.py: Script for inserting sample data into the database.

- interactive_script.py: Interactive script for users to input movie ratings.

- migrate.py: Script for running Alembic migrations.


# Contributing:
If you would like to contribute to the project, please follow the standard GitHub Fork & Pull Request workflow.

Done by Kevin Kiseli found in https://github.com/KevinKiseli/End_of_Phase_3_-Project.git