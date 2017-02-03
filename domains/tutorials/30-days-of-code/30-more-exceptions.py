class Calculator(object):
    def power(self, n, p):
        if (n < 0 or p < 0):
            raise ValueError('n and p should be non-negative')
        else:
            prod = 1
            while p >= 1:
                prod*=n
                p-=1
            return prod

myCalculator=Calculator()
T=int(raw_input())
for i in range(T):
    n,p = map(int, raw_input().split())
    try:
        ans=myCalculator.power(n,p)
        print ans
    except Exception,e:
        print e
