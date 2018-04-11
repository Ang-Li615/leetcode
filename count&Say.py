
def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    if n == 1:
        return '1'
    i = 2
    result = '1'
    while i <= n:
        t = result[0]
        print(t)
        count = 0
        l = ''
        for e in result:
            if t == e:
                count += 1
            else:
                l = l + str(count) + t
                count = 1
                t = e
        l = l + str(count) + e
        result = l
        i += 1
    return result

print(countAndSay(4))