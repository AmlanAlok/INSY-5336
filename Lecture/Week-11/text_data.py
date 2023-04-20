import unittest


text = 'Arlington'
sentence = 'Arlington is a beautiful city'


class MyTestCase(unittest.TestCase):

    def test_1(self):

        self.assertEqual('ARLINGTON', text.upper())

        print(sentence.title())
        self.assertEqual('Arlington Is A Beautiful City', sentence.title())

        print(sentence.split())
        print(''.join(sentence))

    def test_2(self):

        s = sentence
        s.lower()

        v = []
        c = 0
        vowels = 'aeiouAEIOU'

        for x in s:
            if x in vowels:
                c += 1
                if x not in v:
                    v.append(x)

        print(v, c)

    def test_3(self):
        pass





if __name__ == '__main__':
    unittest.main()
