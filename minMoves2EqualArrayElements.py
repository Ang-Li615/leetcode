# class Solution:
#     def minMoves(self, nums):
#         nums = sorted(nums)
#         total = sum(nums)
#         l = len(nums)
#         steps = 0
#         # if set(nums) == 2:
#         #     steps = max(set(nums)) - min(set(nums))
#         #     return steps
#         nums1 = [x+1 for x in nums[0:l-2]]
#         nums1.append(nums[-1])
#         nums = sorted(nums1)
#         while len(set(nums)) != 1:
#             nums1 = [x + 1 for x in nums[0:l - 2]]
#             nums1.append(nums[-1])
#             nums = sorted(nums1)
#             steps = steps + 1
#         return steps



# def minMoves(nums):
#     nums = sorted(nums)
#     total = sum(nums)
#     l = len(nums)
#     steps = 0
#     if len(set(nums)) == 2:
#         steps = max(set(nums)) - min(set(nums))
#         return steps
#
#
#
#
#     while True:
#         print(total)
#         if total % l == 0:
#             print('yay')
#             if total / l >= nums[-1]:
#                 print('ha')
#                 return steps
#         steps += 1
#         total += (l-1)
#
#
# a = minMoves([-100,0,100])
# print(a)


def minMoves(nums):
    nums = sorted(nums)
    total = sum(nums)
    l = len(nums)
    steps = 0
    # if set(nums) == 2:
    #     steps = max(set(nums)) - min(set(nums))
    #     return steps
    while len(set(nums)) != 1:
        nums1 = [x + 1 for x in nums[0:l - 1]]
        nums1.append(nums[-1])
        nums = sorted(nums1)
        steps += 1
    return steps

a = minMoves([-100,0,100])
print(a)


class Solution:
    def minMoves(nums):
        nums = sorted(nums)
        total = sum(nums)
        l = len(nums)
        steps = 0
        if set(nums) == 2:
            steps = max(set(nums)) - min(set(nums))
            return steps
        while len(set(nums)) != 1:
            nums1 = [x + 1 for x in nums[0:l - 1]]
            nums1.append(nums[-1])
            nums = sorted(nums1)
            steps += 1
        return steps