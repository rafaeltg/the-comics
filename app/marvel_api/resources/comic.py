

class Comic:

    def __init__(self, id, title, description, characters=None):
        self._id = id
        self._title = title
        self._desc = description
        self._chars = characters

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._desc

    @property
    def characters(self):
        return self._chars

    @characters.setter
    def characters(self, value):
        self._chars = value

    @staticmethod
    def from_json(comic_json):
        c = Comic(
            id=comic_json['id'],
            title=comic_json['title'],
            description=comic_json['description']
        )
        return c
