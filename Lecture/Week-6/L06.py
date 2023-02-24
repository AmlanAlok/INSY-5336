import unittest


class MyTestCase(unittest.TestCase):

    def test_01(self):
        nums = [10, 20, 30, 25, 9]
        res = list(filter(lambda x: x % 2 == 0, nums))
        # print(res)
        # self.assertEqual(True, True)

    def test_02(self):
        str = 'ArlingtonA'
        res = list(filter(lambda x: x == 'A', str))
        self.assertEqual(['A', 'A'], res)
        self.assertEqual(['A', 'A'], list(filter(lambda x: 'A' in x, str)))
        self.assertEqual(['A', 'A'], list(filter(lambda x: x == 'A', str)))
        self.assertEqual(2, len(list(filter(lambda x: x == 'A', str))))

    def test_03(self):
        from itertools import zip_longest
        fname = ['Naruto', 'Sasuke', 'Sakura']
        lname = ['Uzumaki', 'Uchiha', 'Haruno']

        name = list(zip(fname, lname))
        # print(name)
        self.assertEqual([('Naruto', 'Uzumaki'), ('Sasuke', 'Uchiha'), ('Sakura', 'Haruno')], name)

    def test_04(self):
        from functools import reduce
        nums = [10, 20, 30]
        res = reduce(lambda x, y: x + y, nums)
        print(res)

    def test_05(self):
        from functools import reduce
        nums = ['I', 'like', 'UTA']
        res = reduce(lambda x, y: x + y, nums)
        print(res)

    def test_E01(self):
        a = [1, 2, 3]
        b = [5, 6, 7]

        res = list(map(lambda x, y: x + y, a, b))
        # print(res)
        self.assertEqual([6, 8, 10], list(map(lambda x, y: x + y, a, b)))


if __name__ == '__main__':
    unittest.main()
