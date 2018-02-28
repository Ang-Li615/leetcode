# class Solution:
#     def countBinarySubstrings(self, s):
#         l = len(s)
#         count = 0
#         for i in range(l-1):
#             change = 0
#             j = 0
#         while j < l-1-i and change < 2:
#             if s[i+j] != s[i+j+1]:
#                 change += 1
#             if change == 1:
#                 if len(s[i:i+j+2].strip('0')) == len(s[i:i+j+2].strip('1')):
#                     count = count + 1
#             j = j + 1
#         return count
#
#
# class Solution:
#     def countBinarySubstrings(self, s):
#         l = len(s)
#         count = 0
#         for i in range(l):
#             for j in range(i + 1, l, 2):
#                 change = 0
#                 for k in range(i + 1, j + 1):
#                     if s[k] != s[k - 1]:
#                         change = change + 1
#
#                 if change == 1:
#                     if len(s[i:j + 1].strip('0')) == len(s[i:j + 1].strip('1')):
#                         count = count + 1
#         return count

#
# s = "100111001"
# l = len(s)
# count = 0
# L = []
# for i in range(l-1):
#     j = i+1
#     while j < l:
#         print([i, j])
#         s1 = s[i:j+1]
#         s2 = s[i:j+1]
#         print([s1,s2])
#         if len(s1.replace('0','')) == len(s2.replace('1','')):
#             L.append(s[i:j+1])
#         j = j + 2
# LL  = []
# for e in L:
#     if '01' in e and '10' in e:
#         pass
#     else:
#         LL.append(e)
#
# print(LL)

s = '1101100110001'
group = []
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count = count + 1
    else:
        group.append(count)
        count = 1

group.append(count)

sum = 0
for j in range(len(group)-1):
    for n in range(1, min(len(group[j]),len(group[j+1]))+1):
        sum = sum + 1


