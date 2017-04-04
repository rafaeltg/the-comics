import os
import unittest
from unittest.mock import patch
from ..base import MarvelApi, Character


class MarvelAPITests(unittest.TestCase):

    def setUp(self):
        self.marvel_api = MarvelApi()
        os.environ['MARVEL_PUBLIC_KEY'] = '123'
        os.environ['MARVEL_PRIVATE_KEY'] = '456'

    @patch('app.marvel_api.base.MarvelApi._get')
    def test_get_invalid_character(self, mocked_get):
        mocked_get.return_value = []
        char = self.marvel_api.get_character('test')
        self.assertIsNone(char)

    @patch('app.marvel_api.base.MarvelApi._get')
    def test_get_valid_character(self, mocked_get):
        mocked_get.return_value = [
            {
                'id': 12,
                'name': 'Deadpool',
                'thumbnail': {
                    'path': 'test',
                    'extension': 'jpg'
                },
                'comics': {
                    'items': [
                        {'resourceURI': 'test/123'}
                    ]
                }
            }
        ]

        char = self.marvel_api.get_character('Deadpool')
        self.assertIsNotNone(char)
        self.assertEqual(char.name, 'Deadpool')
        self.assertEqual(char.id, 12)
        self.assertEqual(char.thumbnail, 'test.jpg')
        self.assertListEqual(char.comics, ['123'])

    @patch('app.marvel_api.base.MarvelApi._get')
    def test_get_comic_characters(self, mocked_get):
        mocked_get.return_value = [
            {
                'id': 12,
                'name': 'Deadpool',
                'thumbnail': {
                    'path': 'test',
                    'extension': 'jpg'
                },
                'comics': {
                    'items': [
                        {'resourceURI': 'test/123'}
                    ]
                }
            },
            {
                'id': 23,
                'name': 'Hulk',
                'thumbnail': {
                    'path': 'test',
                    'extension': 'jpg'
                },
                'comics': {
                    'items': [
                        {'resourceURI': 'test/123'}
                    ]
                }
            }
        ]

        chars = self.marvel_api.get_comic_characters('123')
        self.assertEqual(chars[0].name, 'Deadpool')
        self.assertEqual(chars[0].id, 12)
        self.assertEqual(chars[0].thumbnail, 'test.jpg')
        self.assertListEqual(chars[0].comics, ['123'])

        self.assertEqual(chars[1].name, 'Hulk')
        self.assertEqual(chars[1].id, 23)
        self.assertEqual(chars[1].thumbnail, 'test.jpg')
        self.assertListEqual(chars[1].comics, ['123'])

    @patch('app.marvel_api.base.MarvelApi._get')
    @patch('app.marvel_api.base.MarvelApi.get_comic_characters')
    def test_get_comic(self, mocked_get_comic_characters, mocked_get):
        mocked_get.return_value = [
            {
                "id": 12,
                "title": "test",
                "description": "test123",

            }
        ]

        mocked_get_comic_characters.return_value = [Character(123, 'Deadpool', 'test.jpg', ['12'])]

        comic = self.marvel_api.get_comic('12')
        self.assertEqual(comic.id, 12)
        self.assertEqual(comic.title, 'test')
        self.assertEqual(comic.description, 'test123')
        self.assertEqual(len(comic.characters), 1)
        self.assertEqual(comic.characters[0].id, 123)
        self.assertEqual(comic.characters[0].name, 'Deadpool')
        self.assertEqual(comic.characters[0].thumbnail, 'test.jpg')
        self.assertListEqual(comic.characters[0].comics, ['12'])

    @patch('time.strftime')
    def test_aut(self, mocked_strftime):
        mocked_strftime.return_value = '12345'
        self.assertEqual(self.marvel_api._auth(), 'ts=12345&apikey=123&hash=9668c12c30b216f5d9765e27cf7c341f')


if __name__ == '__main__':
    unittest.main()
