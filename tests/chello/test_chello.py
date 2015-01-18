import unittest
from chello import hello


class TestCHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), 'hello world')

