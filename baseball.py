# class Solution:
#     def calPoints(self, ops):
#         n = len(ops)
#         for i in reversed(range(n)):
#             if ops[i] == 'C':
#                 ops.remove(ops[i])
#                 ops.remove(ops[i-1])
#
#         n1 = len(ops)
#         for i in reversed(range(n1)):
#             if ops[i] == 'D':
#                 ops[i] = int(ops[i-1])*2
#
#         for i in reversed(range(n1)):
#             if ops[i] == '+':
#                 ops[i] = int(ops[i-1]) + int(ops[i-2])
#
#         sum = 0
#         for i in ops:
#             sum = sum + int(i)
#
#         return sum
#
# def calPoints(ops):
#     n = len(ops)
#     for i in reversed(range(n)):
#         if ops[i] == 'C':
#             ops.remove(ops[i])
#             ops.remove(ops[i - 1])
#
#     n1 = len(ops)
#     for i in reversed(range(n1)):
#         if ops[i] == 'D':
#             ops[i] = int(ops[i - 1]) * 2
#
#     for i in range(n1):
#         if ops[i] == '+':
#             ops[i] = int(ops[i - 1]) + int(ops[i - 2])
#
#     sum = 0
#     for i in ops:
#         sum = sum + int(i)
#
#     return sum
#
# ops = ["5","-2","4","C","D","9","+","+"]
# calPoints(ops)

# ops = ["36","28","70","65","C","+","33","-46","84","C"]
# i = len(ops) - 1
# while i >= 0:
#     print(i)
#     print(ops[i])
#     if ops[i] == 'C':
#         del ops[i]
#         print(ops)
#         ops.remove(ops[i - 1])
#         print(ops)
#         i = i - 1
#     i = i - 1
#
# print(ops)

def calPoints(ops):
    i = 0
    while i < len(ops):
        if ops[i] == 'C':
            del ops[i]
            del ops[i - 1]
            i = i - 1
            continue
        i = i + 1

    n = len(ops)
    for i in reversed(range(n)):
        if ops[i] == 'C':
            ops.remove(ops[i])
            ops.remove(ops[i - 1])

    n1 = len(ops)
    for i in range(n1):
        if ops[i] == '+':
            ops[i] = int(ops[i - 1]) + int(ops[i - 2])
        if ops[i] == 'D':
            ops[i] = int(ops[i - 1]) * 2

    print(ops)
    sum = 0
    for i in ops:
        sum = sum + int(i)

    return sum
ops = ["-60","D","-36","30","13","C","C","-33","53","79"]
a = calPoints(ops)
print(a)