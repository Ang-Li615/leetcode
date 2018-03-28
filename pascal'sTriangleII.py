class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        L = []
        i = 0
        while i <= rowIndex:
            if i == 0:
                LL = [1]
                L.append(LL)
            elif i == 1:
                LL = [1,1]
                L.append(LL)
            else:
                L1 = L[-1]
                LL = []
                LL.append(1)
                for j in range(len(L1)-1):
                    LL.append(L1[j]+L1[j+1])
                LL.append(1)
                L.append(LL)
            i += 1
        return L[-1]
