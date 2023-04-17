user_count = int(input())
# print(user_count)


z = {}
y = {}
already = {}

for _ in range(user_count):
    n = int(input())
    nums = input()
    # print(n, nums)

    total_sum = 0

    if nums in already:
        print(already[nums])
    else:
        for k in range(1, n + 1):
            total = 0
            i = 0
            j = k

            while j <= n:
                st = nums[i:j]
                # correct till here
                # print(st)

                g = {}

                for s in st:
                    if s in g:
                        g[s] += 1
                    else:
                        g[s] = 1

                val2 = list(g.values())
                keys2 = list(g.keys())
                # print(val)
                r = ''
                for k, v in zip(keys2, val2):
                    r += str(k)

                # if st in z:
                if r in y:
                    # total_sum += z[st]
                    total_sum += y[r]
                    # print('used')
                else:

                    d = {}

                    for s in st:
                        if s in d:
                            d[s] += 1
                        else:
                            d[s] = 1

                    unique_count = len(list(d.keys()))
                    # print(st, unique_count)
                    total_sum += unique_count

                    z[st] = unique_count

                    val = list(d.values())
                    keys = list(d.keys())
                    # print(val)
                    m = ''
                    for k, v in zip(keys, val):
                        m += str(k)
                    # print(m)
                    y[m] = unique_count

                i += 1
                j += 1
        # print('----')
        print(total_sum)
        # print(y)

        already[nums] = total_sum

