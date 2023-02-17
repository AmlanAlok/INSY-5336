import unittest


class MyTestCase(unittest.TestCase):


    def test_something(self):
        res = lambda x, y: x + y
        self.assertEqual(5, res(2, 3))

    def test_multiply(self):
        res = lambda x, y: x * y
        self.assertEqual(14, res(7, 2))


if __name__ == '__main__':
    unittest.main()
