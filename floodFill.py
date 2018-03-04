class Solution:
    def floodFill(self, image, sr, sc, newColor):
        self.image = image
        self.s = set()
        self.s.add((sr,sc))
        self.r = len(image)
        self.c = len(image[0])
        self.findConnect([sr,sc])
        for (i,j) in self.s:
            image[i][j] = newColor
        return image









    def findConnect(self,L):
        l = []
        for [i,j] in L:
            p_l = (i,j-1)
            p_r = (i,j+1)
            p_u = (i-1,j)
            p_d = (i+1,j)
            if j > 0 and p_l not in self.s:
                if self.image[i][j-1] == self.image[i][j]:
                    l.append(p_l)
                    self.s.add(p_l)
            if j < self.c - 1 and p_r not in self.s:
                if self.image[i][j+1] == self.image[i][j]:
                    l.append(p_r)
                    self.s.add(p_r)
            if i > 0 and p_u not in self.s:
                if self.image[i-1][j] == self.image[i][j]:
                    l.append(p_u)
                    self.s.add(p_u)
            if i < self.r - 1 and p_d not in self.s:
                if self.image[i+1][j] == self.image[i][j]:
                    l.append(p_d)
                    self.s.add(p_d)

        if l != []:
            return self.findConnect(l)














        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """