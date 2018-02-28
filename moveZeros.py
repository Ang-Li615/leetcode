class Solution:
    def moveZeroes(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count = count + 1

        for j in range(count):
            nums.remove(0)

        for k in range(count):
            nums.append(0)



