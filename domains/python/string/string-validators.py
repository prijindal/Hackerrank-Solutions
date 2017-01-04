S = input()

found = False
for i in S:
    if i.isalnum():
        found = True
        break
print(found)

found = False
for i in S:
    if i.isalpha():
        found = True
        break
print(found)

found = False
for i in S:
    if i.isdigit():
        found = True
        break
print(found)

found = False
for i in S:
    if i.islower():
        found = True
        break
print(found)

found = False
for i in S:
    if i.isupper():
        found = True
        break
print(found)
