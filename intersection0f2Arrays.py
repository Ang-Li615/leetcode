class Solution:
    def intersect(self, nums1, nums2):
        dict1 = {i: 0 for i in nums1}
        dict2 = {i: 0 for i in nums2}
        for i in nums1:
            dict1[i] += 1
        for i in nums2:
            dict2[i] += 1
        L = []
        for key in dict1:
            if key in dict2:
                times = min(dict1[key], dict2[key])
                for i in range(times):
                    L.append(key)

        return L

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
