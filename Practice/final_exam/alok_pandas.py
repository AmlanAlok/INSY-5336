import unittest
import pandas as pd


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('\n')

    def test_1(self):
        name = ['John', 'Smith', 'Abraham']
        age = [30, 40, 50]
        state = ['Texas', 'Oregon', 'Florida']

        # t = zip(name, age, state)       # return <zip object at 0x7fa5a8c24900>

        df = pd.DataFrame(zip(name, age, state), columns=['Name', 'Age', 'State'])
        print(df)
        print(df.to_string())
        pass

    def test_2(self):
        print(pd.__version__)
        df = pd.read_csv('polo.csv')
        print(df)

    def test_3(self):
        '''
        A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
        '''
        mydataset = {
            'cars': ["BMW", "Volvo", "Ford"],
            'passings': [3, 7, 2]
        }

        myvar = pd.DataFrame(mydataset)

        print(myvar)

    def test_4(self):
        '''
        A Pandas Series is like a column in a table.
        It is a one-dimensional array holding data of any type.
        '''
        a = [1, 7, 2]
        myvar = pd.Series(a)
        print(myvar)
        print(myvar[0])
        print(myvar[1])
        print(myvar[2])
        # print(myvar[3])     #   ValueError: 3 is not in range

    def test_5(self):
        a = [1, 7, 2]
        myvar = pd.Series(a, index=["x", "y", "z"])
        print(myvar)
        print(myvar['x'])
        print(myvar['y'])
        print(myvar['z'])

    def test_6(self):
        calories = {"day1": 420, "day2": 380, "day3": 390}
        myvar = pd.Series(calories)
        print(myvar)

    def test_7(self):
        calories = {"day1": 420, "day2": 380, "day3": 390}
        myvar = pd.Series(calories, index=["day1", "day2"])     # this will not read the 3rd data point
        print(myvar)

    def test_8(self):
        data = {
            "calories": [420, 380, 390],
            "duration": [50, 40, 45]
        }

        # load data into a DataFrame object:
        df = pd.DataFrame(data)

        print(df)
        print(df.loc[0])
        # print(df.loc[3])    # ValueError: 3 is not in range
        # print(df[0])        # throws KeyError

        # use a list of indexes:
        print(df.loc[[0, 1]])

    def test_9(self):
        # Named Indexes
        data = {
            "calories": [420, 380, 390],
            "duration": [50, 40, 45]
        }

        df = pd.DataFrame(data, index=["day1", "day2", "day3"])

        print(df)
        # refer to the named index:
        print(df.loc["day2"])
        print(pd.options.display.max_rows)


if __name__ == '__main__':
    unittest.main()
