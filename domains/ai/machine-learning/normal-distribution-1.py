import math
def pdf(x):
    epower = -((x - u)**2)/2*(s)**2
    value = math.exp(epower)
    return (1/(s*math.sqrt(2*pi)))*value

u = 30
s = 4
pi = math.pi
ans = 0
for x in range(0,40):
    ans+=pdf(x)
print(ans)
ans = 0
for x in range(0,20):
    ans+=pdf(x)
ans = 1-ans
print(ans)

ans = 0
for x in range(30,35):
    ans+=pdf(x)
print(ans)
