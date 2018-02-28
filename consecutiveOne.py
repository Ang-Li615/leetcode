class Solution:
    def findMaxConsecutiveOnes(self, nums):
        L = [-1]
        for i, j in enumerate(nums):
            if j == 0:
                L.append(i)
        L.append(len(nums))


        m = 0
        for i in range(len(L)):
            if i + 1 < len(L):
                m = max(L[i+1] - L[i] - 1,m)

        return m










        """
        :type nums: List[int]
        :rtype: int
        """