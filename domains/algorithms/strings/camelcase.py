s = input()

count = 0
if len(s) > 0:
    count += 1

for i in s:
    if i.upper() == i:
        count+=1

print(count)
