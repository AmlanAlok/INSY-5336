n = int(input())
# print(n)

nums = input().split()

for i in range(len(nums)):
    nums[i] = int(nums[i])
# print(nums)

ans = [0] * len(nums)

i = len(nums) - 1
ans[i] = 0
high = nums[i]
low = nums[i]
i -= 1

# while i >= 0:
#     x = nums[i]
#     if x > high and x > low:
#         ans[i] += 1
#         high = x
#     if x <= high:
#         ans[i] += 1
#         low = x
#     if x > low:
#         ans[i] += 1

#     if x < low:
#         high = low
#         low = x
#     # if x >

#     i -= 1

p = ''
for q in ans:
    p += str(q) + ' '
print(p)
# final = ' '.join(ans)
# print(final)