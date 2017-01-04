from itertools import permutations
def lexiBigger(str):
    str = tuple(str)
    s = sorted(str)
    p = list(permutations(s))
    l = len(p)
    ans = None
    for i in range(l):
        # print(p[i+1])
        if p[i] == str:
            if p[i+1] != str:
                ans = p[i+1]
            break;
    if not ans:
        return "no answer"
    else:
        return ''.join(ans)
t = int(input())

for i in range(t):
    print(lexiBigger(input()))
