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
        ans = ''
        user = 'i love utA'
        vowels = 'aeiouAEIOU'
        for i in user:
            if i in vowels:
                ans += i

        self.assertEqual('ioeuA', ans)
        self.assertEqual(5, len(ans))

    'find the longest word in a string'

    def test_08_my_way(self):
        ans = ''
        user = 'i love uta'
        m, t = 0, 0
        temp = ''
        for i in user:
            if i == ' ':
                if len(temp) > m:
                    ans, m = temp, t
                    temp, t = '', 0
            else:
                temp += i
                t += 1

        if len(temp) > m:
            ans, m = temp, t
            temp, t = '', 0
        print(ans)

        self.assertEqual('love', ans)
        self.assertEqual(4, m)

    def test_08_prof(self):
        ans = ''
        user = 'i love uta'
        longest = ''
        for i in user.split():
            if len(i) > len(longest):
                longest = i

        self.assertEqual('love', longest)

    'Exercise 2 in Class_3_Loops'

    def test_exercise2(self):

        lo, hi = 0, 10

        if lo > hi:
            lo, hi = hi, lo
        subtotal = []
        s = 0
        for i in range(lo, hi + 1):
            s += i
            print(s)
            subtotal.append(s)

        print(subtotal)
        self.assertEqual(220, sum(subtotal))
