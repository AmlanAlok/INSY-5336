import unittest


class MyTestCase(unittest.TestCase):

    def test_1(self):
        x = (1, 2, 3, 4, 5)

        self.assertEqual(15, sum(x))
        self.assertEqual(3, sum(x) / len(x))

    def test_2(self):
        x = ('a', 'b', 'c', 'd')
        output = []
        for i in range(len(x) - 1, -1, -1):
            output.append(x[i])

        output = tuple(output)

        self.assertEqual(('d', 'c', 'b', 'a'), output)
        self.assertEqual(('d', 'c', 'b', 'a'), tuple(reversed(x)))

    def test_31(self):
        x = (1, 2, 3)
        y = (4, 5, 6)
        ans = 0
        i = 0
        while i < len(x):
            ans += x[i] * y[i]
            i += 1

        self.assertEqual(32, ans)

    def test_32(self):
        a = (1, 2, 3)
        b = (4, 5, 6)

        self.assertEqual(32, sum(list(map(lambda x, y: x*y, a, b))))

    def test_33(self):
        a = (1, 2, 3)
        b = (4, 5, 6)
        self.assertEqual([4, 10, 18], [x*y for x, y in zip(a, b)])
        self.assertEqual(32, sum([x*y for x, y in zip(a, b)]))

    def test_4(self):
        a = ['India', 'USA']
        for i, v in enumerate(a):
            print(i, '-', v)

    def test_5(self):
        a = [(1, 3), (2, 1), (4, 5), (2, 2)]

        self.assertEqual([(2, 1), (2, 2), (1, 3), (4, 5)], sorted(a, key=lambda x: (x[1], x[0]), reverse=False))




if __name__ == '__main__':
    unittest.main()
