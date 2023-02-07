import unittest


class MyTestCase(unittest.TestCase):
    """While loop"""

    def test_01(self):
        i = 0
        while i < 10:
            print(i)
            i += 1

    def test_02(self):
        a = [1, 2, 3]
        for i in a:
            print(i)

    def test_03(self):

        ans = []

        for i in range(5):
            ans.append(i)

        self.assertEqual([0, 1, 2, 3, 4], ans)
        ans.clear()

        for i in range(4, 9):
            ans.append(i)

        self.assertEqual([4, 5, 6, 7, 8], ans)
        ans.clear()

        for i in range(1, 10, 2):
            ans.append(i)

        self.assertEqual([1, 3, 5, 7, 9], ans)
        ans.clear()

        for i in range(10, 0, -1):
            ans.append(i)

        self.assertEqual([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], ans)
        ans.clear()

    # def test_04(self):
