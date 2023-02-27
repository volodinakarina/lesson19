from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_by_genre_id(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def create(self, movie_data):
        entity = Movie(**movie_data)
        self.session.add(entity)
        self.session.commit()
        return entity

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_data):
        movie = self.get_one(movie_data.get("id"))
        movie.title = movie_data.get("title")
        movie.description = movie_data.get("description")
        movie.trailer = movie_data.get("trailer")
        movie.year = movie_data.get("year")
        movie.rating = movie_data.get("rating")
        movie.genre_id = movie_data.get("genre_id")
        movie.director_id = movie_data.get("director_id")

        self.session.add(movie)
        self.session.commit()
