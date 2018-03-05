class Solution(object):
    def containsDuplicate(self, nums):
        dict = {i:0 for i in nums}
        for i in nums:
            dict[i] += 1
        for key in dict:
            if dict[key] > 1:
                return True
        return False








        """
        :type nums: List[int]
        :rtype: bool
        """
