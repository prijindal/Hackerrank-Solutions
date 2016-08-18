time = input()
hh,mm,ss = time.split(':')
day = ss[2:]
ss = ss[:2]


if hh == '12':
    if day == 'AM':
        hh='00'

if day == 'PM':
    if hh!='12':
        hh=int(hh)
        hh+=12
        hh=str(hh)

print('{}:{}:{}'.format(hh,mm,ss))
