import unittest


class MyTestCase(unittest.TestCase):
    """Slicing"""

    def test_c01(self):
        a = [1, 2, 3, 4, 5, 6, 7, ]

        self.assertEqual(a[2:6:1], [3, 4, 5, 6])
        self.assertEqual(a[-2:-6:-1], [6, 5, 4, 3])
        self.assertEqual(a[-2:-6:-2], [6, 4])
        self.assertEqual(a[-2:-6:-3], [6, 3])
        self.assertEqual(a[-2:-6], [])
        self.assertEqual(a[-2:-6:1], [])
        self.assertEqual(a[-2:], [6, 7])
        self.assertEqual(a[:-6], [1])

        print(a[-2:-6])
        print(a[-2:-6:1])

    def test_c02(self):
        a = [1, 2, 3]

        b = [i for i in a]
        self.assertEqual([1, 2, 3], b)
        self.assertEqual([1, 4, 9], [i ** 2 for i in a])

        x = [i for i in range(1, 101) if i % 2 == 0 and i % 3 == 0]
        print(x)

    """List comprehension"""

    def test_03(self):
        lst = [10, 20, 30, 40, 50, 60, 70]

        self.assertEqual([10, 20, 30, 40, 50, 60, 70], [i for i in lst])
        self.assertEqual([60, 70], [i for i in lst if i > 50])
        self.assertEqual([60, 70], list(filter(lambda x: x > 50, lst)))

        self.assertEqual(['smaller', 'smaller', 'smaller', 'smaller', 'greater', 'greater', 'greater'],
                         ['greater' if i > 40 else 'smaller' for i in lst])

        self.assertEqual(['greater', 'greater'],
                         ['greater' if i > 40 else 'smaller' for i in lst if i > 50])

        self.assertEqual([[10, 20, 30, 40, 50, 60, 70],
                          [10, 20, 30, 40, 50, 60, 70],
                          [10, 20, 30, 40, 50, 60, 70],
                          [10, 20, 30, 40, 50, 60, 70],
                          [10, 20, 30, 40, 50, 60, 70],
                          [10, 20, 30, 40, 50, 60, 70],
                          [10, 20, 30, 40, 50, 60, 70]], [[i for i in lst] for i in lst])


if __name__ == '__main__':
    unittest.main()
