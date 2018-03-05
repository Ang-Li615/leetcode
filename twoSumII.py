class Solution:
    def twoSum(self, numbers, target):
        l = len(numbers)
        i = 0
        j = l-1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i,j]
            elif numbers[i] + numbers[j] > target:
                j = j - 1
            elif numbers[i] + numbers[j] < target:
                i = i + 1
        return False

#
#
# def twoSum(numbers, target):
#     l = len(numbers)
#     i = 0
#     j = l - 1
#     while i < j:
#         if numbers[i] + numbers[j] == target:
#             return [i+1, j+1]
#         elif numbers[i] + numbers[j] > target:
#             j = j - 1
#         elif numbers[i] + numbers[j] < target:
#             i = i + 1
#     return False
#
#
# numbers = [2,7,11,15]
# target = 9
# a = twoSum(numbers,target)
# print(a)

