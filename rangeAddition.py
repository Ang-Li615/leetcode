class Solution:
    def maxCount(self, m, n, ops):
        m1 = m
        n1 = n
        for i in range(len(ops)):
            m1 = min(m1,ops[i][0])
            n1 = min(n1,ops[i][1])

        return m1*n1
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """