s=raw_input()

n,c=raw_input().split()
n=int(n)

s=s[:n]+c+s[n+1:]
print s
