import requests
import hashlib
import time
import os
from .resources import Character, Comic


BASE_URL = 'https://gateway.marvel.com/v1/public'


class MarvelApi:

    def __init__(self):
        self.base_url = BASE_URL
        self._attrib_html = None

    @property
    def attribution_html(self):
        return self._attrib_html

    def get_character(self, name):
        url = self.base_url + '/characters?name={}&'.format(name)
        chars_json = self._get(url)
        return Character.from_json(chars_json[0]) if len(chars_json) > 0 else None

    def get_comic(self, id):
        url = self.base_url + '/comics/{}?'.format(id)
        comic_json = self._get(url)[0]
        c = Comic.from_json(comic_json)
        c.characters = self.get_comic_characters(id)
        return c

    def get_comic_characters(self, id):
        url = self.base_url + '/comics/{}/characters?'.format(id)
        chars_json = self._get(url)
        return [Character.from_json(c) for c in chars_json]

    def _get(self, url):
        resp = requests.get(url+self._auth())
        resp_json = resp.json()
        self._attrib_html = resp_json['attributionHTML']
        return resp_json['data']['results']

    def _auth(self):
        timestamp = time.strftime("%s")
        public_key = self._get_env_var('MARVEL_PUBLIC_KEY')
        private_key = self._get_env_var('MARVEL_PRIVATE_KEY')
        hash_val = hashlib.md5(str(timestamp + private_key + public_key).encode('utf-8')).hexdigest()
        return "ts=%s&apikey=%s&hash=%s" % (timestamp, public_key, hash_val)

    @staticmethod
    def _get_env_var(v):
        if v not in os.environ:
            raise KeyError('Environment variable %s not declared!' % v)
        return str(os.environ[v])
