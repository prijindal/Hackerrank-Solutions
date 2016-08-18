def testcase():
    N, M, S = [int(x) for x in input().split()]

    ans = M%N
    ans += (S - 1)
    if ans > N:
        ans-=N
    if ans == 0:
        ans = N
    print(ans)

t = int(input())
for i in range(t):
    testcase()
