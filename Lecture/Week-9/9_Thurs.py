import unittest


class Course:
    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings

    def show(self):
        print(self.name)
        print(self.ratings)
        return self.name, self.ratings

    def average(self):
        avg = sum(self.ratings) / len(self.ratings)
        print(avg)
        return avg


class BankAccount:
    def __init__(self, num, name, balance):
        self.num = num
        self.name = name
        self.balance = balance

    def deposit(self, add_amount):
        self.balance += add_amount
        return self.balance

    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            return self.balance
        else:
            print('Insufficient funds')
            return 'Insufficient funds'


class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def show_info(self):
        print(self.id, self.name, self.salary)
        return self.id, self.name, self.salary

    def yearly_salary(self):
        yearly_salary = self.salary*12
        print(yearly_salary)
        return yearly_salary

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary


class Student:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def add_course(self, c):
        self.courses.append(c)

    def getGPA(self):
        all_grades = []
        for c in self.courses:
            all_grades.append(c.grade)

        if all_grades:
            return sum(all_grades)/len(all_grades)
        return 0


class Course2:
    def __init__(self, cname, grade):
        self.cname = cname
        self.grade = grade


class MyTestCase(unittest.TestCase):

    def test_5(self):
        python = Course2('Python', 4.0)
        java = Course2('Java', 3.5)
        php = Course2('PHP', 3.0)
        s = Student('Alok', [python, java, php])
        self.assertEqual(3.5, s.getGPA())
        s2 = Student('Zoro', [])
        self.assertEqual(0, s2.getGPA())

    def test_2(self):
        c = Course('Java', [3, 4, 5])
        self.assertEqual(('Java', [3, 4, 5]), c.show())
        self.assertEqual(4, c.average())

    def test_3(self):
        a = BankAccount(1, 'Alok', 1000)
        self.assertEqual(1050, a.deposit(50))
        self.assertEqual(950, a.withdraw(100))
        self.assertEqual('Insufficient funds', a.withdraw(1000))

    def test_4(self):
        a = Employee('Alok', 1, 1000)
        self.assertEqual((1, 'Alok', 1000), a.show_info())
        self.assertEqual(12000, a.yearly_salary())
        self.assertEqual(1200, a.raise_salary(200))



if __name__ == '__main__':
    unittest.main()
