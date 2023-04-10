import unittest


class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f'{self.name} is having food now')

class Mammal(Animal):
    def __init__(self, name, fur_color):
        Animal.__init__(self, name)
        self.fur_color = fur_color

    def sleep(self):
        print(f'{self.name} is now sleeping')


class Reptile(Animal):
    def __init__(self, name, scale_color):
        Animal.__init__(self, name)
        self.scale_color = scale_color

class Platypus(Mammal, Reptile):
    def __init__(self, name, fur_color, scale_color):
        Mammal.__init__(self, name, fur_color)
        Reptile.__init__(self, name, scale_color)


class MyTestCase(unittest.TestCase):

    def test_something(self):
        perry = Platypus('Perry', 'green', 'brown')
        perry.eat()
        perry.sleep()
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
