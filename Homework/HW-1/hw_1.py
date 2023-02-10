import unittest


def ans_1(st1, st2, st3):

    if st3 == st2 + st1:
        return 'They are equal'
    else:
        return 'They are not equal'


def find_max(nums):

    if nums is []:
        return None

    m = nums[0]

    for i in nums:
        if i > m:
            m = i

    return m


def find_avg(nums):

    if nums is []:
        return None

    average = 0.0

    for i in nums:
        average += i

    average = average/len(nums)

    return average


def ans_2(count):
    t = ['first', 'second', 'third', 'fourth']
    p = 0
    user = [7, 10, 1]
    # while count > 0:
    #     x = print(input('Enter ' + t[p] + ' number'))
    #     user.append(x)
    #     count -= 1

    return find_avg(user), find_max(user)





class MyTestCase(unittest.TestCase):


    def test_01(self):
        self.assertEqual('They are equal', ans_1('you!', 'Thank', 'Thankyou!'))
        self.assertEqual('They are not equal', ans_1('you2!', 'Thank', 'Thankyou!'))

    def test_02(self):
        self.assertEqual((6.0, 10), ans_2(3))