class Solution:
    def readBinaryWatch(self, num):
        list1 = [8, 4, 2, 1]
        list2 = [32, 16, 8, 4, 2, 1]
        if num == 0:
            return ['0:00']
        L = []
        for i in range(4):
            j = num - i
            if j >= 0 and j <= 5:
                L.append([i,j])
        LL = []
        for e in L:
            if e[0] == 0:
                h = ['0:']
            if e[0] == 1:
                h = ['1:','2:','4:','8:']
            if e[0] == 2:
                h = ['3:','5:','6:','9:','10:']
            if e[0] == 3:
                h = ['7:','11:']

            if e[1] == 0:
                m = ['00']
            if e[1] == 1:
                m = ['01','02','04','08','16','32']
            if e[1] == 2:
                m = ['03','05','06','09','10','12','17','18','20','24','33','34','36','40','48']
            if e[1] == 3:
                m = ['07','11','13','14','19','21','22','25','26','28','35','37','38','41','42','44','49','50','52','56']
            if e[1] == 4:
                m = ['15','23','27','29','30','39','43','45','46','51','53','54','57','58']
            if e[1] == 5:
                m = ['31','47','55','59']

            for i in h:
                for j in m:
                    LL.append(i+j)

        return LL





        """
        :type num: int
        :rtype: List[str]
        """
