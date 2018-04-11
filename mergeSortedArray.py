class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n == 0:
            return None
        if m == 0 and n != 0:
            i = 0
            for e in nums2:
                nums1[i] = e
                i += 1
        if m != 0 and n == 0:
            return None
        i = 0
        j = 0
        while j < n and i < m + j:
            if nums1[i] < nums2[j]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
                i += 1
        while j < n:
            nums1[i] = nums2[j]
            j += 1
            i += 1