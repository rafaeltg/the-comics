

class Character:

    def __init__(self, id, name, thumbnail, comics):
        self._id = id
        self._name = name
        self._thumb = thumbnail
        self._comics = comics

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def thumbnail(self):
        return self._thumb

    @property
    def comics(self):
        return self._comics

    @staticmethod
    def from_json(char_json):
        c = Character(
            id=char_json['id'],
            name=char_json['name'],
            thumbnail=char_json['thumbnail']['path']+'.'+char_json['thumbnail']['extension'],
            comics=[c['resourceURI'].split('/')[-1] for c in char_json['comics']['items']]
        )
        return c
