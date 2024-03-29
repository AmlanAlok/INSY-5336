import unittest
import random
import numpy as np



class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('\n')

    def test_1(self):
        x = random.random()     # Python uses the Mersenne Twister as the core generator
        # print(x)
        self.assertEqual(True, 0.0 <= x <= 1.0)

        x = random.randrange(5)
        # print(x)
        self.assertEqual(True, 0 <= x < 5)

        x = random.randrange(5, 10)
        # print(x)
        self.assertEqual(True, 5 <= x < 10)

        x = random.randint(0, 10)
        print(x)
        self.assertEqual(True, 0 <= x <= 10)

    def test_2(self):
        x = random.randrange(10, 10, -1)     # ValueError: empty range for randrange() (10, 10, 0)
        print(x)
        self.assertEqual(True, 0 <= x <= 10)

        x = random.randrange(5, 10, 0)      # ValueError: zero step for randrange()

    def test_3(self):
        rand = random.randrange(10, 9, -1)
        print(rand)

    def test_4(self):
        x = np.random.randn(8)
        print(x)




if __name__ == '__main__':
    unittest.main()
