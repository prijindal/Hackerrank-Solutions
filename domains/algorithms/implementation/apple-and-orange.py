s, t = [int(i) for i in raw_input().split(' ')]
a, b = [int(i) for i in raw_input().split(' ')]
m, n = [int(i) for i in raw_input().split(' ')]

da = [int(i) for i in raw_input().split(' ')]
db = [int(i) for i in raw_input().split(' ')]

counta = 0
countb = 0

for i in da:
    x = a + i
    if x >= s and x <= t:
        counta += 1
for i in db:
    x = b + i
    if x >= s and x <= t:
        countb += 1
print(counta)
print(countb)
