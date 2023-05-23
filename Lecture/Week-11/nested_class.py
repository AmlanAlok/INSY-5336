import unittest

"""Question kj"""
class Vehicle:

    def __init__(self, x):
        self.x = x

    class Car:
        def __init__(self, y):
            self.y = y


class MyTestCase(unittest.TestCase):

    def test_something(self):

        z = Vehicle(5)
        q = z.Car(2)
        # p = Car(9)


        # self.assertEqual(True, False)

    def test_x(self):
        if 1:
            print('A')
        else:
            print('Z')


if __name__ == '__main__':
    unittest.main()