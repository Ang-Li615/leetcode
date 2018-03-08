class Solution:
    def checkRecord(self, s):
        n_A = 0
        for i in s:
            if i == 'A':
                n_A += 1
            if n_A > 1:
                return False

        l = len(s)
        n_L = 1
        for i in range(l-1):
            if s[i] == 'L' and s[i+1] == 'L':
                n_L += 1
            else:
                n_L = 1

            if n_L > 2:
                return False

        return True