class Solution:
    def __init__(self):
        pass

    def letterCasePermutation(self, S):
        if len(S) > 12:
            return 'Error'
        else:
            count = 0
            for s in S:
                if s >= 'A' and s <= 'z':
                    count = count + 1
            return count

a = Solution()
t = a.letterCasePermutation('Ac123')
print(t)


