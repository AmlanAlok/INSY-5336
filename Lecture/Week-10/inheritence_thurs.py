import unittest


class Player:
    def score(self):
        pass


class Soccer_player(Player):
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def score(self, goals):
        self.goals = goals
        print(f'{self.name} scored {self.goals} foals in the last season.')


class Cricket_player(Player):
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def score(self, runs):
        self.runs = runs
        print(f'{self.name} scored {self.runs} runs in the last season.')





class MyTestCase(unittest.TestCase):

    def test_1(self):
        s = Soccer_player('Alok', 1)
        s.score(5)
        c = Cricket_player('Philip', 9)
        c.score(100)
        self.assertEqual(5, s.goals)
        self.assertEqual(100, c.runs)


if __name__ == '__main__':

    unittest.main()
