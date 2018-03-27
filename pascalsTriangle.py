class Solution:
    def generate(self, numRows):
        L = []
        i = 1
        while i <= numRows:
            if i == 1:
                LL = [1]
                L.append(LL)
            if i == 2:
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
        return L









        """
        :type numRows: int
        :rtype: List[List[int]]
        """
