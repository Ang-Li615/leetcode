class Solution:
    def intersection(self, nums1, nums2):
        nums = set(nums1) & set(nums2)
        return list(nums)



        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """