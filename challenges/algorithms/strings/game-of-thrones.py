# Wrong Answer
def possiblePalindrome(message):

    CHARS = 'abcdefghijklmnopqrstuvwxyz'
    CHARDICT = {}
    for i in range(26):
        CHARDICT[CHARS[i]]=0

    for i in message:
        CHARDICT[i]+=1

    Pal = True
    if len(message)%2==0:
        for i in CHARDICT:
            if CHARDICT[i]%2!=0:
                pal = False
                break
    else:
        odds = 0
        for i in CHARDICT:
            if CHARDICT[i]%2==1:
                odds+=1
        if odds!=1:
            Pal = False
    return 'YES' if Pal else 'NO'

print(possiblePalindrome(input()))
