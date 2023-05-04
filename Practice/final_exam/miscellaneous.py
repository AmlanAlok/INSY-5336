import unittest
import numpy as np


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('\n')

    def test_1(self):
        x = ['uta', 'unt', 'utd', 'mit', 'ucla']
        print(x[-2:-4:-2])
        # self.assertEqual(True, False)

    def test_2(self):
        x = np.arange(10)
        print(x)

    def test_3(self):
        for i in range(1, 5, -1):
            print('x')

    def test_4(self):
        dc = {3: 1, 2: 2, 0: 3}
        dc2 = {i**2:k**3 for i, k in dc.items() if k >= 3}
        print(dc2)  # {0: 27}

    def test_5(self):
        x = (1, 7)
        print(x**2)     # TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'

    def test_6(self):
        len = 6
        print(f'Charge: {len*4.00:.2f}')

    def test_7(self):
        print(9%2)


if __name__ == '__main__':
    unittest.main()
