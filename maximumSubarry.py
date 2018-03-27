class Solution:
    def maxSubArray(self, nums):
        L = []
        l = len(nums)
        m = 0
        for i in range(l):
            if nums[i] < 0:
                if m != 0:
                    L.append(m)
                L.append(nums[i])
                m = 0
            else:
                m += nums[i]
        if m != 0:
            L.append(m)
        print(L)
        l = len(L)
        LL = []
        for i in range(l):
            if L[i] >= 0:
                LL.append(i)
        print(LL)
        l = len(LL)
        if l == 0:
            return max(nums)
        if l == 1:
            return L[LL[0]]
        LLL = []
        for i in range(l-1):
            for j in range(i+1,l,1):
                sum = 0
                for z in range(LL[i],LL[j]+1):
                    sum += L[z]
                LLL.append(sum)
        A = max(LLL)
        return max(A,max(L))










        """
        :type nums: List[int]
        :rtype: int
        """