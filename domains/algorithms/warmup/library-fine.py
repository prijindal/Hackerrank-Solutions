import datetime

def convertDay(list):
    return datetime.datetime(day = list[0], month = list[1], year = list[2])

actualDate = [int(i) for i in input().split()]
expectedDate = [int(i) for i in input().split()]

actual = convertDay(actualDate)
expected = convertDay(expectedDate)

ans = 0
if actual.year > expected.year:
    ans = 10000
elif actual.month > expected.month and actual.year == expected.year:
    ans=(actual.month - expected.month)*500
elif actual.day > expected.day and actual.month == expected.month:
    ans = ans=(actual.day - expected.day)*15
else:
    ans = 0


print(ans)
