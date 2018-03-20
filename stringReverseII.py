# class Solution:
#     def reverseStr(self, s, k):
#         l = len(s)
#         i = 0
#         n = l // k
#         r = l % k
#         s_r = ''
#
#         if n == 0:
#             s_r += s[::-1]
#
#         for i in range(n):
#             start = i*k
#             end = (i+1)*k
#             s_t = s[start:end:1]
#             if i % 2 == 0:
#                 s_r += s_t[::-1]
#             else:
#                 s_r += s_t
#
#         if r != 0:
#             s_t = s[end::1]
#             s_r += s_t
#
#         return s_r

def reverseStr(s, k):
    l = len(s)
    i = 0
    n = l // k
    print(n)
    r = l % k
    print(r)
    s_r = ''

    if n == 0:
        s_r += s[::-1]

    for i in range(n):
        start = i*k
        end = (i+1)*k
        print(start,end)
        s_t = s[start:end:1]
        print(s_t)
        if i % 2 == 0:
            s_r += s_t[::-1]
            print(s_r)
        else:
            s_r += s_t
            print(s_r)

    if r != 0:
        print('ya')
        s_t = s[end::1]
        print(s_t)
        s_r += s_t
        print(s_r)

    return s_r

s = "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"
k = 39

a = reverseStr(s,k)
print(a)
