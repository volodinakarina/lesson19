from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, genre_data):
        return self.dao.create(genre_data)

    def update(self, genre_data):
        self.dao.update(genre_data)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)
