class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {i:[] for i in nums}
        for tag,i in enumerate(nums):
            dict[i].append(tag)
        for key in dict:
            l = len(dict[key])
            if l > 1:
                i = 0
                while i < l-1:
                    if abs(dict[key][i+1]-dict[key][i]) <= k:
                        return True
                    else:
                        i += 1
                        continue
        return False
