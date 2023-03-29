# def fac(num):
#     if num == 1:
#         return 1
#     else:
#         return num * fac(num-1)
#
# print(fac(5))


# from functools import reduce
# num = 5
# nums = range(1, num+1)
#
# ans = reduce(lambda x, y: x*y, nums)
# print(ans)

# class Nissan:
#     def __init__(self, type, year):
#         self.__type = type
#         self.__year = year
#
#
# nissan = Nissan("Compact", 2022)
# print(nissan._Nissan__year)

# text = " \" I like UTA \" "
# print(text)
# print(text.strip())

# set1 = {10, 20, 30}
# set2 = {15, 25, 35}
# set3 = set2.difference(set1)
# print(set3)

# set1 = set([2,5])
# set1.add(10, 15)
# print(set1)

# import pandas as pd
# lst1 = ['p', 'j']
# lst2 = [9, 8]
# df = pd.DataFrame([lst1, lst2], columns=['N', 'A'])
# df.head()


# lst = ['Even' if i%2==1 else 'odd' for i in range(0, 4)]
# print(lst)


# x = [int(i) for i in input('Enter two numbers: ').split()]
# print(x+x)
#
# print(input('Enter two numbers: ').split())


# text = 'I love UTA uta'
# text = text.split()
# count = {}
#
# for i in text:
#     count[i] = count.get(i, 0) + 1
#
# print(count)
