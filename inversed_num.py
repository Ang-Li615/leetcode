class Solution:
    def reverse(self, x):
        L = []
        for n in str(abs(x)):
            L.append(n)
        s = str()
        for n1 in L[::-1]:
            s = s + n1
        if x < 0:
            s = '-' + s

        xnew = int(s)