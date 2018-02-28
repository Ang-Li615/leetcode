class Solution:
    def singleNumber(self, nums):
        dict = {i: 0 for i in nums}
        for i in nums:
            dict[i] = dict[i] + 1
        return list(dict.keys())[list(dict.values()).index(1)]
