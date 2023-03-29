import unittest


class MyTestCase(unittest.TestCase):

    def test_1(self):
        a = [1, 1, 2, 3, 4, 4]
        self.assertEqual([1, 2, 3, 4], list(set(a)))

    def test_2(self):
        a = {1, 2, 3}
        b = {2, 3, 7}
        c = {5, 6, 1}

        t = [a, b, c]
        self.assertEqual([{1, 2, 3}, {2, 3, 7}, {1, 5, 6}], t)

        s = set()

        for i in t:
            s.update(i)

        self.assertEqual({1, 2, 3, 5, 6, 7}, s)

    def test_3(self):
        st = 'amlan'
        self.assertEqual({'m', 'l', 'a', 'n'}, set(st))
        self.assertEqual(4, len(set(st)))

    def test_4(self):
        a = {1, 2, 3}
        b = {4, 5, 6}
        self.assertEqual(True, True if a.isdisjoint(b) else False)
        a = {1, 2, 3, 4}
        b = {4, 5, 6}
        self.assertEqual(False, True if a.isdisjoint(b) else False)

    def test_extra(self):
        x = 'Amlan Alok'
        y = x.replace(' ', '')
        self.assertEqual('AmlanAlok', y)

    def test_e1(self):
        st = 'Hello World!'
        vowels = 'aeiouAEIOU'
        cleaned = [c for c in st if c not in vowels]
        self.assertEqual(['H', 'l', 'l', ' ', 'W', 'r', 'l', 'd', '!'], cleaned)
        new_st = ''.join(cleaned)
        self.assertEqual('Hll Wrld!', new_st)

    def test_5(self):
        nums = [1, 2, 3, 3, 4, 4, 5]
        seen, duplicates = set(), set()

        for i in nums:
            if i in seen:
                duplicates.add(i)
            else:
                seen.add(i)

        self.assertEqual({3, 4}, duplicates)

    def test_x(self):
        for i in range(5):
            print(i)


if __name__ == '__main__':
    unittest.main()
