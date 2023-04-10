import unittest

'''Multiple Inheritance'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'HI, I am {self.name}. Iam {self.age} years old.')

class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary

    def work(self):
        print(f'Employee {self.id} earns {self.salary} salary.')


class Manager(Person, Employee):

    def __init__(self, name, age, id, salary, dept):
        Person.__init__(self, name, age)
        Employee.__init__(self, id, salary)
        self.dept = dept



class MyTestCase(unittest.TestCase):

    def test_1(self):
        m = Manager('Alok', 28, 1, 100, 'Dev')
        m.introduce()
        m.work()
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
