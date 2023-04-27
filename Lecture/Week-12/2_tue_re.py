import unittest
import re

class MyTestCase(unittest.TestCase):
    def test_something(self):
        text = 'This is the $crazy thing happened during @COVID in 2022'
        z1 = re.sub('\W', ' ', text)
        self.assertEqual(z1, 'This is the  crazy thing happened during  COVID in 2022')
        z2 = re.sub('\d', '', z1)
        self.assertEqual('This is the  crazy thing happened during  COVID in ', z2)
        z3 = re.sub('\s+', '', z2)
        self.assertEqual('This is the  crazy thing happened during  COVID in ', z2)


if __name__ == '__main__':
    unittest.main()
