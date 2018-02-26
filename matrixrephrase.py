class Solution:
    def matrixReshape(self, nums, r, c):
        L = []
        r1 = len(nums)
        c1 = len(nums[0])
        if r1*c1 < r*c:
            return nums
        else:
            i1 = 0
            j1 = 0
            for i in range(r):
                R = []
                for j in range(c):
                    R.append(nums[i1][j1])
                    j1 = j1 + 1
                    if j1 >= c1:
                        j1 = 0
                        i1 = i1 + 1
                L.append(R)
            return L
