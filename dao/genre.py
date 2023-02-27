from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, genre_data):
        entity = Genre(**genre_data)
        self.session.add(entity)
        self.session.commit()
        return entity

    def update(self, genre_data):
        genre = self.get_one(genre_data.get("id"))
        genre.name = genre_data.get("name")

        self.session.add(genre)
        self.session.commit()

    def delete(self, gid):
        genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()
