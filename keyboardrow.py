# class Solution:
#     def findWords(self, words):
#         L = []
#         for w in words:
#             success = True
#             for r in ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']:
#                 if w[0].lower() in r:
#                     for e in w[1:]:
#                         if e not in r:
#                             success = False
#
#             if success:
#                 L.append(w)
#         return L

def findWords(words):
    L = []
    for w in words:
        success = True
        for r in ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']:
            if w[0].lower() in r:
                for e in w[1:]:
                    if e.lower() not in r:
                        success = False

        if success:
            L.append(w)
    return L

words = ['hello', 'Alaska','zZxcvbnm']
L = findWords(words)
print(L)