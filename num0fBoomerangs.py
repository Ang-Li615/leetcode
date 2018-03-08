# class Solution:
#     def numberOfBoomerangs(self, points):
#         L = sorted(points)
#         l = len(points)
#         total = 0
#         for i in range(1,l-1):
#             for j in range(i):
#                 m = L[i][0] - L[j][0]
#                 for k in range(l-1,i,-1):
#                     n = L[k][0] - L[i][0]
#                     if m == n:
#                         if L[j][1] + L[k][1] == 2*L[i][1]:
#                             total += 2
#
#         return total


# def numberOfBoomerangs(points):
#     l = len(points)
#     total = 0
#     for i in range(l):
#         for j in range(l):
#             if j == i:
#                 continue
#             for k in range(j,l):
#                 if k == j or k == i:
#                     continue
#                 print(i,j,k)
#                 xij = (points[i][0] - points[j][0])*(points[i][0] - points[j][0])
#                 yij = (points[i][1] - points[j][1])*(points[i][1] - points[j][1])
#                 xik = (points[i][0] - points[k][0])*(points[i][0] - points[k][0])
#                 yik = (points[i][1] - points[k][1])*(points[i][1] - points[k][1])
#                 if xij + yij == xik + yik:
#                     print('yay')
#                     total += 2
#     return total
#
# points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
# total = numberOfBoomerangs(points)
# print(total)


class Solution:
    def numberOfBoomerangs(self, points):
        l = len(points)
        total = 0
        for i in range(l):
            for j in range(l):
                if j == i:
                    continue
                for k in range(j,l):
                    if k == j or k == i:
                        continue
                    xij = (points[i][0] - points[j][0])*(points[i][0] - points[j][0])
                    yij = (points[i][1] - points[j][1])*(points[i][1] - points[j][1])
                    xik = (points[i][0] - points[k][0])*(points[i][0] - points[k][0])
                    yik = (points[i][1] - points[k][1])*(points[i][1] - points[k][1])
                    if xij + yij == xik + yik:
                        total += 2
        return total


