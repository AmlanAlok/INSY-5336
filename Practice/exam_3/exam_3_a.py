import unittest


class Nissan:
    def __init__(self, type, year):
        self.__type = type
        self.year = year


nissan = Nissan("Compact", 2022)
print(nissan.year)


class MyTestCase(unittest.TestCase):
    """Exam-1"""

    def test_x1(self):
        pass

    def test_1(self):
        t = 0
        for i in range(1, 5):
            s = i ** 2
            t = t + s
        print(t)

    def test_2(self):
        t1 = t2 = 10, 'UTA'
        print(t2)
        print(type(t2))
        print(t1)

    def test_4(self):
        n1 = 100
        n2 = 120
        n3 = 80
        if n1 > 100 and n2 < 110 or n3 > 50:
            print("I did not know it")
        else:
            print("I knew it")

    def test_5(self):
        languages = [['Spanish', 'English'], ['Python', 'Java']]
        for x in languages:
            print("------")
            for x in x:
                print(x)

    def myFunction(self, val):
        if val % 3 == 0 or val % 2 ** 3 < 3:
            return val

    def test_6(self):

        res = filter(self.myFunction, (1, 3, 5, 6, 14))
        print(list(res))

    def test_7(self):

        print(5 % 2 ** 3)

    def test_8(self):
        p = [1, 5, 2, 7, 8]
        fil = list(filter(lambda x: 2 * x + x > 20 + x, p))
        print(fil)

    def test_9(self):
        import pandas as pd
        import numpy as np
        s1 = pd.Series(np.random.randn(6), index=list('abcdef'))
        print(s1)
        # print(s1.iloc['b'])

    def test_10(self):
        pass


if __name__ == '__main__':
    unittest.main()
