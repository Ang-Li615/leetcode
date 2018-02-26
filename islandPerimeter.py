class Solution:
    def islandPerimeter(self, grid):
        r = len(grid)
        c = len(grid[0])
        n = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    count = 0
                    for x in [max(0,i-1), min(r-1,i+1)]:
                        if grid[x][j] == 1 and x != i:
                            count = count + 1
                    for y in [max(0,j-1),min(c-1,j+1)]:
                        if grid[i][y] == 1 and y != j:
                            count = count + 1
                    if count == 1:
                        n = n + 3
                    elif count == 2:
                        n = n + 2
                    elif count == 0:
                        n = n + 4
                    elif count == 3:
                        n = n + 1
                    else:
                        n = n + 0
        return n