import math
def encryptMessage(message):
    message = message.replace(' ','')
    length = len(message)
    lengSqrt = math.sqrt(length)
    rows = math.ceil(lengSqrt)
    columns = math.ceil(lengSqrt)

    answer = []
    for i in range(columns):
        for j in range(rows):
            n = j*columns+i
            if n < length:
                answer.append(message[j*columns+i])
        answer.append(' ')
    return ''.join(answer)


print(encryptMessage(input()))
