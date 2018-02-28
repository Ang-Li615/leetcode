N = 10
dict = {'0':'0', '1':'1', '2':'5', '5':'2', '6':'9', '8':'8', '9':'6'}
count = 0
for n in range(1,N+1):
    goodnum = True
    s = str(n)
    for i in range(len(s)):
        if s[i] not in dict.keys():
            goodnum = False
            break
        else:
            s = s[:i]+dict[s[i]]+s[i+1:]

    if goodnum:
        if str(n) != s:
            count = count + 1

print(count)



