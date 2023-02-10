import unittest


def hello_world():
    print('Hello World!')


def add(x, y):
    return x + y


class MyTestCase(unittest.TestCase):

    def test_01(self):
        hello_world()
        self.assertEqual(9, add(4, 5))
