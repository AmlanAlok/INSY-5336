import unittest


class BankAccount:
    def __init__(self, accNum, balance):
        # _ before the variable makes it protected
        self._accNum = accNum
        self.balance = balance


class MyTestCase(unittest.TestCase):

    def test_something(self):
        ba = BankAccount(1001, 500)
        print(ba.accNum)


if __name__ == '__main__':
    unittest.main()
