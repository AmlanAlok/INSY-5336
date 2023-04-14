import unittest

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    def gear(self):
        print('shifting gear')

class Car(Vehicle):
    def stop(self):
        print('Stoping')


# -----

class Federal(ABC):
    def __init__(self, fed_tax, amount):
        self.fed_tax = fed_tax
        self.amount = amount

    def display(self):
        print('Fed Tax =', self.fed_tax)
        print('Tax Amount =', self.amount*self.fed_tax)

    @abstractmethod
    def pay_tax(self):
        pass

class State(Federal):

    def __init__(self, fed_tax, amount, state_tax):
        super().__init__(fed_tax, amount)
        self.state_tax = state_tax

    def display_state(self):
        print('State Tax =', self.state_tax)
        print('Tax Amount =', self.amount * self.state_tax)

    def calcualte_tax(self):
        fed = self.amount*self.fed_tax
        state = self.amount*self.state_tax
        print('Total tax =', fed + state)
        return fed + state

    def pay_tax(self):
        print('Please pay tax by April')

class MyTestCase(unittest.TestCase):

    def test_2(self):
        s = State(0.10, 100, 0.05)
        s.display()
        s.display_state()
        s.pay_tax()
        s.calcualte_tax()

    def test_something(self):
        car = Car()
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
