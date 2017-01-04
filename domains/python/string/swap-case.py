def swap(ch):
    if ch.islower():
        ch = ch.upper()
    elif ch.isupper():
        ch = ch.lower()
    return ch

L = ''.join([swap(i) for i in input()])
print(L)
