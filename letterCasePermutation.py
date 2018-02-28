class Solution:
    def letterCasePermutation(self, S):
        L = ['']
        for char in S:
            LL = []
            if char.isalpha():
                for s in L:
                    LL.append(s + char.lower())
                    LL.append(s + char.upper())
                L = LL

            else:
                for s in L:
                    LL.append(s + char)
                L = LL

        return L
