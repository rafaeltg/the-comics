import unittest
from app import app


class TheComicsTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index(self):
        res = self.app.get('/')
        self.assertEqual(res.status_code, 200)
        assert b'Deadpool' in res.data

    def test_index_name(self):
        res = self.app.get('/Hulk')
        self.assertEqual(res.status_code, 200)
        assert b'Hulk' in res.data

    def test_index_name_invalid_char(self):
        res = self.app.get('/test')
        self.assertEqual(res.status_code, 404)
        assert b'Character not found' in res.data
        assert b'Could not found a character named "test"' in res.data


if __name__ == '__main__':
    unittest.main()
