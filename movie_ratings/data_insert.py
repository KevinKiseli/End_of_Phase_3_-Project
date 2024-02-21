# movie_ratings/data_insert.py


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from database import Movie, MovieDetails, Rating, Base, User


def create_user(session, username):
    new_user = User(username=username)
    session.add(new_user)
    session.commit()


def create_movie(session, title, genres):
    existing_movie = session.query(Movie).filter_by(title=title).first()

    if not existing_movie:
        new_movie = Movie(title=title, genres=genres)
        session.add(new_movie)
        session.commit()
        return new_movie
    else:
        return existing_movie


def input_movie_details(session, movie, director, release_date):
    existing_details = session.query(MovieDetails).filter_by(movie_id=movie.id).first()

    if not existing_details:
        new_details = MovieDetails(movie_id=movie.id, director=director, release_date=release_date)
        session.add(new_details)
        session.commit()


def rate_movie(session, username, movie_id, rating):
    user = session.query(User).filter_by(username=username).first()
    if not user:
        create_user(session, username)
        user = session.query(User).filter_by(username=username).first()

    existing_rating = session.query(Rating).filter_by(username=username, movie_id=movie_id).first()

    if not existing_rating:
        new_rating = Rating(username=username, movie_id=movie_id, ratings=rating, timestamp=datetime.utcnow())
        session.add(new_rating)
        session.commit()


if __name__ == "__main__":
    engine = create_engine('sqlite:///movie_ratings.db')
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Analog example:

    inception = create_movie(session, "Inception", "Sci-Fi")
    input_movie_details(session, inception, "Christopher Nolan", datetime(2010, 7, 16))
    rate_movie(session, "Rose Flower", inception.id, 4.8)

    rush_hour = create_movie(session, "Rush Hour 1", "Comedy")
    input_movie_details(session, rush_hour, "Brett Ratner", datetime(1998, 9, 18))
    rate_movie(session, "Clinton Money", rush_hour.id, 4.5)

    django_unchained = create_movie(session, "Django Unchained", "Action")
    input_movie_details(session, django_unchained, "Quentin Tarantino", datetime(2012, 12, 25))
    rate_movie(session, "Kevin Kiseli", django_unchained.id, 4.9)

    the_irishman = create_movie(session, "The Irishman", "Crime")
    input_movie_details(session, the_irishman, "Martin Scorsese", datetime(2019, 11, 1))
    rate_movie(session, "Peter Pan", the_irishman.id, 4.9)

    maestro = create_movie(session, "Maestro", "Romance")
    input_movie_details(session, maestro, "Bradley Cooper", datetime(2023, 9, 2))
    rate_movie(session, "Fiona Piano", maestro.id, 3.8)

    # any additional movies go here


    session.close()


