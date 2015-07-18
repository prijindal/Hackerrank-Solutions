A = raw_input()
B = raw_input()

lena=len(A)
lenb=len(B)

ans=0
for i in range(0,lena-lenb+1):
    if B == A[i:i+lenb]:
        ans+=1
print ans
