import unittest


class MyTestCase(unittest.TestCase):

    def test_01(self):

        d4 = {i: i*i for i in range(1, 11) if i*i > 50}
        print(d4)
        self.assertEqual({8: 64, 9: 81, 10: 100}, {i: i*i for i in range(1, 11) if i > 5 and i*i > 50})
        self.assertEqual({8: 64, 9: 81, 10: 100}, {i: i * i for i in range(1, 11) if i * i > 50})

    def test_02(self):

        d = {'A': '12345', 'B': '54321', 'C': '67890'}

        x = {k: v for k, v in d.items() if v[0] == '5'}
        print(x)

    def test_01(self):

        s = 'AabbbCC C'

        d = {}

        for c in s.lower():
            if 97 <= ord(c) <= 122:
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1

        print(d)

        x = {k: s.lower().count(k) for k in s.lower() if 97 <= ord(k) <= 122}
        print(x)




if __name__ == '__main__':
    unittest.main()
