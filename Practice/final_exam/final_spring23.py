import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('\n')

    def test_1(self):
        for i in range(5):
            print(i)
        else:
            print('Done')

    def test_2(self):
        for i in range(5):
            if i == 2:
                break
            print(i)
        else:
            print('Done')

    def test_3(self):
        i = 0
        while i < 5:
            print(i)
            i += 1
        else:
            print('Done')

    def test_4(self):
        i = 0
        while i < 5:
            if i == 2:
                break
            print(i)
            i += 1
        else:
            print('Done')

    def test_4(self):
        a = [10, 20, 30]
        b = ['a', 'b', 'c']

        x = [i + j for i, j in zip(a, b)]
        print(x)

    def test_5(self):
        a = (1,2,3)
        b = a + (4, 5)
        print(b)

    def test_5(self):
        for i in range(1, 5):
            for j in range(1, 5):
                if i * j > 10:
                    break
                print(i*j)
            print('Inner')
        print('outer')


if __name__ == '__main__':
    unittest.main()
