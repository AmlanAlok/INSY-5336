import unittest


class MyTestCase(unittest.TestCase):

    def test_1(self):
        path = './dummy.txt'
        with open(path, 'r') as file:
            content = file.read()
            print(content)
            file.close()

        lines = content.split('\n')
        self.assertEqual(3, len(lines))     # line count

        words = content.split()
        self.assertEqual(7, len(words))     # word count

        self.assertEqual(37, len(content))

    def test_2(self):
        path = './grades.txt'
        with open(path, 'r') as file:
            content = file.read()

        lines = content.split('\n')
        lines = [x.strip().split(':') for x in lines]
        lines.sort()
        # lines = sorted(lines, key= lambda x: [x[1], x[0]])
        for i in lines:
            print(i)

    def test_3(self):
        path = './inventory.txt'
        with open(path, 'r') as file:
            content = file.read()

        lines = content.split('\n')
        lines = [line.strip().split(',') for line in lines]

        total = 0

        # for i in range(1, len(lines)):
        #     line = lines[i]
        for line in lines[1:]:
            # line = lines[i]
            price, qty = float(line[2]), int(line[3])
            # price, qty = line[2], line[3]
            print(price, qty)
            total += price * qty

        self.assertEqual(5470.40, total)






if __name__ == '__main__':
    unittest.main()
