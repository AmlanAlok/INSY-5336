import unittest


def main():
    x = input('Enter:')
    print(x)




class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    main()
    # unittest.main()
