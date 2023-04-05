import unittest


class Person():
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hello ', self.name)


class Student(Person):
    def __init__(self, sId, name):
        super().__init__(name)
        self.student_id = sId

    def study(self):
        print('Student ', self.name, 'with sId = ', self.student_id, ' is studying')
        return self.student_id, self.name


class Teacher(Person):
    def __init__(self, tId, name):
        super().__init__(name)
        self.teacher_id = tId

    def teach(self):
        print('Student ', self.name, 'with sId = ', self.teacher_id, ' is teaching')
        return self.teacher_id, self.name


# -----------------------------------------

# class BankAccount:
#     def __init__(self, balance, interest_rate):
#         self.balance = balance
#         self.interest_rate = interest_rate
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):

class Shape:
    def calculate_area(self):
        return


class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def calculate_area(self):
        return 0.5 * self.base * self.height


class MyTestCase(unittest.TestCase):

    def test_1(self):
        amlan = Student(1, 'Amlan')
        self.assertEqual((1, 'Amlan'), amlan.study())

        alok = Teacher(2, 'Alok')
        self.assertEqual((2, 'Alok'), alok.teach())

    def test_3(self):
        r = Rectangle(2,4)
        print(r.calculate_area())


if __name__ == '__main__':
    unittest.main()
