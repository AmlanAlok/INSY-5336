user_count = int(input())
# print(user_count)

for _ in range(user_count):
    n = int(input())
    nums = input()
    # print(n, nums)

    total_sum = 0

    for k in range(1, n + 1):
        total = 0
        i = 0
        j = k

        while j <= n:
            st = nums[i:j]
            # correct till here
            # print(st)

            d = {}

            for s in st:
                if s in d:
                    d[s] += 1
                else:
                    d[s] = 1

            unique_count = len(list(d.keys()))
            # print(st, unique_count)
            total_sum += unique_count

            i += 1
            j += 1
    # print('----')
    print(total_sum)



#https://www.hackerrank.com/contests/utaspring23-2/challenges/penguins-peeping-the-penguins

# https://www.hackerrank.com/contests/utaspring23-2/challenges/uniqueness-of-a-lineup



