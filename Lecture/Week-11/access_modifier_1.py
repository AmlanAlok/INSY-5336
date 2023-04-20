import unittest


class Continent:
    def __init__(self, name, size, population):
        self.name = name
        self._size = size
        self.__population = population

class Asia(Continent):
    def __init__(self, name, size, population, climate):
        super().__init__(name, size, population)
        self.climate = climate



class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = Asia('Alok', 100, 10)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
