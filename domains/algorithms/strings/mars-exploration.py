s = input()
l = len(s)
sos = 'SOS'*int(l/3)

count = 0
for i in range(0, l):
    if s[i] != sos[i]:
        count+=1

print(count)
