import unittest


class MyTestCase(unittest.TestCase):

    def test_01(self):
        st = 'polo'
        self.assertEqual('polo', st[:])
        self.assertEqual('polo', st[0:])
        self.assertEqual('olo', st[1:])

        x = 'p'
        self.assertEqual('p', x[:])
        self.assertEqual('p', x[0:])
        self.assertEqual('p', x[0:1])

        y = ''
        self.assertEqual('', y[:])
        self.assertEqual('', y[0:])

    def test_02(self):

        a = []
        out = True if a else False
        self.assertEqual(False, out)
        a = [1]
        out = True if a else False
        self.assertEqual(True, out)

        a = None
        out = True if a else False
        self.assertEqual(False, out)

        a = ''
        out = True if a else False
        self.assertEqual(False, out)
        a = 'polo'
        out = True if a else False
        self.assertEqual(True, out)

    def test_03(self):

        x = 'a' + str(1)
        print(x)


if __name__ == '__main__':
    unittest.main()
