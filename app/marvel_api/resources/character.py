import json


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
        id = char_json['id'] if 'id' in char_json else ''
        name = char_json['name'] if 'name' in char_json else ''
        comics = char_json['comics']['items'] if 'comics' in char_json else []
        c = Character(
            id=id,
            name=name,
            thumbnail=char_json['thumbnail']['path']+'.'+char_json['thumbnail']['extension'],
            comics=[c['resourceURI'].split('/')[-1] for c in comics],
        )
        return c
