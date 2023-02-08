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

        for i in range(lo, hi + 1):
            ans.append(i)
        # print(ans)

        self.assertEqual([1, 2, 3, 4, 5], ans)
        ans.clear()

    "print from 10 to 1"

    def test_02_B(self):
        ans = []
        for i in range(10, 0, -1):
            ans.append(i)

        self.assertEqual([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], ans)
        ans.clear()

    def test_03(self):
        ans = []
        x = 10
        for i in range(0, x + 1, 2):
            ans.append(i)

        self.assertEqual([0, 2, 4, 6, 8, 10], ans)
        ans.clear()

    'print all odd integers in a range and sum them all'

    def test_04(self):
        ans = []
        x = 10
        sum = 0
        for i in range(0, x + 1):
            if i % 2 == 1:
                ans.append(i)
                sum += i

        self.assertEqual([1, 3, 5, 7, 9], ans)
        self.assertEqual(25, sum)
        ans.clear()

    'print all num between lo and hi and find its sum'

    def test_05(self):
        ans = []
        lo, hi = 0, 10
        sum = 0
        for i in range(lo, hi + 1):
            ans.append(i)
            sum += i

        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ans)
        self.assertEqual(55, sum)
        ans.clear()

    'find largest number in list'

    def test_06(self):

        user = [1, 7, 89, 45]

        if user is []:
            return 'empty array'
        m = user[0]
        for i in user:
            if i > m:
                m = i

        self.assertEqual(m, max(user))

    'program to print the number of vowels in a string'
    def test_07(self):
        ans = []
        user = 'i love uta'
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in user:
            if i in vowels:
                ans.append(i)

        self.assertEqual(['i', 'o', 'e', 'u', 'a'], ans)
        self.assertEqual(5, len(ans))
