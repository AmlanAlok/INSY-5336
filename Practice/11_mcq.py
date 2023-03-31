import unittest


class MyTestCase(unittest.TestCase):

    def test_1(self):
        lst = [3, 6, 9]
        dc = {}
        print(type(dc))

        for i in lst:
            dc = i*i
            print(type(dc))

        print(dc)
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
