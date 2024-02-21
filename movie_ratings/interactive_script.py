# movie_ratings/interactive_script.py


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from database import create_movie, input_movie_details, rate_movie, create_user, User, Session

def get_user_input():
    while True:
        username = input("Enter 2 names: ")
        names = username.split()

        if len(names) == 2:
            break
        else:
            print("Please enter two names.")

    title = input("Enter the movie title: ")
    genres = input("Enter the movie genres: ")
    director = input("Enter the movie director: ")
    release_date_str = input("Enter the release date (YYYY-MM-DD): ")
    rating = float(input("Enter your rating (0.0 to 5.0): "))

    return " ".join(names), title, genres, director, release_date_str, rating


def main():
    engine = create_engine('sqlite:///movie_ratings.db')
    Session.configure(bind=engine)
    session = Session()

    username, title, genres, director, release_date_str, rating = get_user_input()


    # Create user
    user = session.query(User).filter_by(username=username).first()
    if not user:
        create_user(session, username)
        user = session.query(User).filter_by(username=username).first()

    # Create movie
    movie = create_movie(session, title, genres)

    # Input movie details
    input_movie_details(session, movie, director, datetime.strptime(release_date_str, "%Y-%m-%d"))

    # Rate movie
    rate_movie(session, username, movie.id, rating)

    # Commit changes to the database
    session.commit()

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
