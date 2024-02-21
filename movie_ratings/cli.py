# movie_ratings/cli.py


import sys
import os
import argparse

sys.path.append(os.getcwd())

from database import Session, Movie, MovieDetails, Rating, User


# List movies in movie_ratings.db

def list_movies():
    session = Session()
    movies = session.query(Movie).all()

    if not movies:
        print("No movies found in the database.")
    else:
        print("List of Movies:")
        for movie in movies:
            print(f"{movie.id}: {movie.title} - {movie.genres}")

    session.commit()
    session.close()


# delete movie based on movie id
    
def delete_movie(movie_id):
    session = Session()

    # Retrieve the movie and details
    movie = session.query(Movie).filter_by(id=movie_id).first()

    if not movie:
        print(f"No movie found with ID {movie_id}")
    else:
        print(f"Deleting movie: {movie.title} - {movie.genres}")

        # Delete any details first
        movie_details = session.query(MovieDetails).filter_by(movie_id=movie_id).first()
        if movie_details:
            session.delete(movie_details)

        # Delete movie ratings
        ratings = session.query(Rating).filter_by(movie_id=movie_id).all()
        for rating in ratings:
            session.delete(rating)

        # Delete the movie
        session.delete(movie)
        session.commit()
        print("Movie deleted successfully.")

    session.commit()
    session.close()


# list the different movie ratings
    
def list_user_ratings(username):
    session = Session()
    user = session.query(User).filter_by(username=username).first()

    if not user:
        print(f"No user found with username: {username}")
    else:
        print(f"Movie Ratings for {username}:")
        for rating in user.ratings:
            print(f"Movie: {rating.movie.title}, Rating: {rating.ratings}")

    session.commit()
    session.close()


# Interacting with the movie_ratings.db using the command line interface
    
def main():
    parser = argparse.ArgumentParser(description='Manage a Movie Database')
    parser.add_argument('--list-movies', action='store_true', help='List all movies')
    parser.add_argument('--delete-movie', type=int, help='Delete a movie by ID')
    parser.add_argument('--list-user-ratings', type=str, help='List ratings for a user by username')

    args = parser.parse_args()

    if args.list_movies:
        list_movies()
    elif args.delete_movie:
        delete_movie(args.delete_movie)
    elif args.list_user_ratings:
        list_user_ratings(args.list_user_ratings)



if __name__ == "__main__":
    main()
