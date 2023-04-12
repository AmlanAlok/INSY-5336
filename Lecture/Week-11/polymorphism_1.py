import unittest

'''Example problem'''

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return 'Woof!'


class Cat(Animal):
    def speak(self):
        return 'Meow'
#----------------------------------------------
'''Q1'''
class Vehicle:
    def __init__(self):
        pass

    def start(self):
        print('Start Vehicle')
        pass

    def stop(self):
        pass

class Car(Vehicle):
    def __init__(self):
        pass

    def start(self):
        super().start()
        print('4 wheels')
        return 4


class Motorcycle(Vehicle):
    def __init__(self):
        pass

    def start(self):
        super().start()
        print('2 wheels')
        return 2

'''Q2'''

class Employee:
    def __init__(self, baseSalary):
        self.baseSalary = baseSalary
    def calculate_salary(self):
        return self.baseSalary

class Manager(Employee):
    def __init__(self, baseSalary):
        Employee.__init__(self, baseSalary)
    def calculate_salary(self):
        return self.baseSalary + 10

class Developer(Employee):
    def __init__(self, baseSalary):
        Employee.__init__(self, baseSalary)

    def calculate_salary(self):
        return self.baseSalary + 5


class MyTestCase(unittest.TestCase):

    def test_3(self):
        m = Manager(100)
        self.assertEqual(110, m.calculate_salary())

    def test_2(self):

        v, m = Car(), Motorcycle()
        self.assertEqual(4, v.start())
        self.assertEqual(2, m.start())


    def test_something(self):
        d = Dog()
        c = Cat()
        self.assertEqual('Woof!', d.speak())
        self.assertEqual('Meow', c.speak())



if __name__ == '__main__':
    unittest.main()
