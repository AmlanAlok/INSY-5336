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
        print(df.info())
        print(df.to_string())

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
        print(myvar.columns)
        print(myvar.index)
        print(myvar.shape)
        print(myvar.head(2))
        print(myvar.tail(2))
        print(myvar.sample(2))
        print('--------------')
        print(myvar.describe())
        print('--------------')
        row, col = myvar.shape[0], myvar.shape[1]
        print(f'Row = {row}, Col = {col}')

    def test_32(self):
        '''
        A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
        '''
        mydataset = {
            'cars': "BMW",
            'passings': 3
        }

        myvar = pd.Series(mydataset)

        print(myvar)
        print(myvar['cars'])
        print(myvar['passings'])

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
        myvar = pd.Series(calories, index=["day1", "day2"])  # this will not read the 3rd data point
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

        # iloc is usd for integer based indexing
        print(df.iloc[:, 1])

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

    def test_10(self):
        s1 = pd.Series()
        print(s1)

    def test_11(self):
        s1 = pd.Series([1, 2, 3, 4, 5])
        print(s1)
        print(s1.index)
        print(s1.values)

    def test_12(self):
        age = {'Bob': 45, 'Alex': 55, 'Sarah': 25}
        s3 = pd.Series(age)
        print(s3)
        s4 = pd.Series(age, index=['Sarah', 'Bob', 'Alex', 'Milton'])
        print(s4)

    def test_13(self):
        df1 = pd.DataFrame()
        print(type(df1))
        print(df1)
        print(df1.columns)
        print(df1.index)

    def test_14(self):
        '''ValueError: All arrays must be of the same length'''

        df = pd.DataFrame({
            'Name': ['Abbas', 'Rohit', 'Micky'],
            'Birthyear': [1970, 1984, 2013, 2016]
        })

        df['age'] = df['Birthyear'].apply(lambda x: (2022 - x) + 5)
        print(df['age'])

    def test_15(self):
        pass

    def test_16(self):
        pass

    def test_17(self):
        pass

    def test_18(self):
        pass


if __name__ == '__main__':
    unittest.main()
