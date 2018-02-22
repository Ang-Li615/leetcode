class Solution:
    def reverseWords(self, s):
        s_list = s.split()
        L = []
        for e in s_list:
            L.append(e[::-1])

        s_new = ' '.join(L)
        return s_new