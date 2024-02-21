# movie_ratings/database.py


from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    genres = Column(String(200), nullable=False)

    details = relationship('MovieDetails', back_populates='movie')
    ratings = relationship('Rating', back_populates='movie')


class MovieDetails(Base):
    __tablename__ = 'movie_details'

    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)
    director = Column(String(100))
    release_date = Column(DateTime)

    movie = relationship('Movie', back_populates='details')


class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), ForeignKey('users_table.username'), nullable=False)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)
    ratings = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    movie = relationship('Movie', back_populates='ratings') 
    user = relationship('User', back_populates='ratings')


class User(Base):
    __tablename__ = 'users_table'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)

    ratings = relationship('Rating', back_populates='user')


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


def delete_movie(session, movie_id):
    # Delete movie details and ratings
    movie = session.query(Movie).get(movie_id)
    if movie:
        # Delete details
        details = session.query(MovieDetails).filter(MovieDetails.movie_id == movie_id).all()
        for detail in details:
            session.delete(detail)
        # Delete ratings
        ratings = session.query(Rating).filter(Rating.movie_id == movie_id).all()
        for rating in ratings:
            session.delete(rating)
        # Delete movie
        session.delete(movie)
        session.commit()


# SQLite is the database
engine = create_engine('sqlite:///movie_ratings.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)





