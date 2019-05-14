import unittest
from ApiHelper import *


class TestApiHelper(unittest.TestCase):

    def setUp(self):
        api = ApiHelper()
        self.resp = api.star_war_characters(1)

    def test_non_empty_list(self):
        self.assertTrue(self.resp)

    def test_empty_list(self):
        pass

if __name__ == '__main__':
    unittest.main()