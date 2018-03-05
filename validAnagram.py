# class Solution:
#     def isAnagram(self, s, t):
#         if s == t:
#             if len(set(s)) < 2:
#                 return True
#             else:
#                 return False
#
#         if len(s) != len(t):
#             return False
#         for i in s:
#             if i not in t:
#                 return False
#             else:
#                 t.replace(i,'',1)
#         if t == '':
#             return True
#         else:
#             return False
#
#
#
#
#
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """


def isAnagram(s, t):
    if s == t:
        if len(set(s)) < 2:
            return True
        else:
            return False

    if len(s) != len(t):
        return False
    for i in s:
        if i not in t:
            return False
        else:
            t = t.replace(i,'',1)
            print(t)
    if t == '':
        return True
    else:
        return False

a = isAnagram('ab','ba')
print(a)

