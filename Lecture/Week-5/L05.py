import unittest


class MyTestCase(unittest.TestCase):

    def test_something(self):
        res = lambda x, y: x + y
        self.assertEqual(5, res(2, 3))

    def test_multiply(self):
        res = lambda x, y: x * y
        self.assertEqual(14, res(7, 2))

    def test_upper(self):
        res = lambda x: x.upper()
        self.assertEqual('ARLINGTON', res('Arlington'))

    def test_reverse(self):
        y = [1, 3, 2]
        res = lambda x: sorted(x, reverse=True)
        self.assertEqual([3, 2, 1], res(y))

    def test_warm_up_1(self):
        res = lambda x, y: x * y
        self.assertEqual(14, res(7, 2))

    def test_warm_up_2(self):
        res = lambda x: len(x)
        self.assertEqual(3, res('UTA'))

    def test_warm_up_3(self):
        res = lambda x: 'positive' if x > 0 else 'non-positive'
        self.assertEqual('positive', res(1))
        self.assertEqual('non-positive', res(-1))

    def test_warm_up_4(self):
        pass

    def test_warm_up_5(self):
        pass


if __name__ == '__main__':
    unittest.main()
