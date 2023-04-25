import re

text = 'I love UTD. Because UTD is awesome. This is 2023'
z1 = re.sub('UTD', 'UTA', text)
# print(z1)
assert z1 == 'I love UTA. Because UTA is awesome. This is 2023'

z2 = re.sub('[a-z]', '', text)
print(z2)
assert z2 == 'I **** UTD. B****** UTD ** *******. T*** ** 2023'

t2 = '2023 is a great year'
z3 = re.sub('\d', '', t2)
assert z3 == ' is a great year'
# print(z3)







