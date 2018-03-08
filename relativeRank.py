class Solution:
    def findRelativeRanks(self, nums):
        sortnums = sorted(nums)
        l = len(nums)
        dict = {}
        for i in range(l):
            dict[sortnums[i]] = l - i

        L = []
        for score in nums:
            if dict[score] == 1:
                L.append('Gold Medal')
            elif dict[score] == 2:
                L.append('Silver Medal')
            elif dict[score] == 3:
                L.append('Bronze Medal')
            else:
                L.append(str(dict[score]))
        return L





        """
        :type nums: List[int]
        :rtype: List[str]
        """
