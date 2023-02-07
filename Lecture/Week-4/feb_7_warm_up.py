import unittest


class MyTestCase(unittest.TestCase):

    """print from 1 to 10"""
    def test_01(self):
        ans = []

        for i in range(1, 11):
            ans.append(i)

        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ans)
        ans.clear()

    '''Ask user to input the lo and hi values'''
    def test_02(self):
        ans = []

        # lo = int(input('Enter lower threshold: '))
        # hi = int(input('Enter higher threshold: '))

        lo, hi = 1, 5

        for i in range(lo, hi+1):
            ans.append(i)
        print(ans)

        # self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ans)
        # ans.clear()

    "print from 10 to 1"
    def test_03(self):
        ans = []
        for i in range(10, 0, -1):
            ans.append(i)

        self.assertEqual([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], ans)
        ans.clear()

