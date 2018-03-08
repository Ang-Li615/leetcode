# class Solution:
#     def imageSmoother(self, M):
#         M1 = M
#         r = len(M)
#         c = len(M[0])
#         for i in range(r):
#             for j in range(c):
#                 list1 = [(i, j), (i, j - 1), (i, j + 1), (i - 1, j), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j),
#                          (i + 1, j - 1), (i + 1, j + 1)]
#                 list2 = [(i - 1, j), (i - 1, j - 1), (i - 1, j + 1)]  # i == 0
#                 list3 = [(i + 1, j),(i + 1, j - 1), (i + 1, j + 1)]              # i == r-1
#                 list4 = [(i,j-1),(i-1,j-1),(i+1,j-1)]                 # j == 0
#                 list5 = [(i,j+1),(i-1,j+1),(i+1,j+1)]                 # j == c-1
#                 s = set(list1)
#                 if i == 0:
#                     s = s - set(list2)
#                 if i == r-1:
#                     s = s - set(list3)
#                 if j == 0:
#                     s = s - set(list4)
#                 if j == c-1:
#                     s = s - set(list5)
#                 L = list(s)
#                 l = len(L)
#                 sum = 0
#                 for e in L:
#                     sum += M[e[0]][e[1]]
#                 M1[i][j] = sum // l
#         return M1

def imageSmoother(M):
    M1 = []
    r = len(M)
    c = len(M[0])

    for i in range(r):
        L1 = []
        for j in range(c):
            list1 = [(i, j), (i, j - 1), (i, j + 1), (i - 1, j), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j),
                     (i + 1, j - 1), (i + 1, j + 1)]
            list2 = [(i - 1, j), (i - 1, j - 1), (i - 1, j + 1)]  # i == 0
            list3 = [(i + 1, j),(i + 1, j - 1), (i + 1, j + 1)]              # i == r-1
            list4 = [(i,j-1),(i-1,j-1),(i+1,j-1)]                 # j == 0
            list5 = [(i,j+1),(i-1,j+1),(i+1,j+1)]                 # j == c-1
            s = set(list1)
            if i == 0:
                s = s - set(list2)
            if i == r-1:
                s = s - set(list3)
            if j == 0:
                s = s - set(list4)
            if j == c-1:
                s = s - set(list5)
            L = list(s)
            l = len(L)
            sum = 0
            for e in L:
                sum += M[e[0]][e[1]]
            smoother = sum // l
            L1.append(smoother)
        print(L1)
        M1.append(L1)


    return M1

M = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
M1 = imageSmoother(M)
print(M1)