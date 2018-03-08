class Solution:
    def findRestaurant(self, list1, list2):
        com = set(list1) & set(list2)
        com = list(com)
        if com == []:
            return []
        l1 = len(list1)
        l2 = len(list2)
        m = l1 + l2
        dict = {}
        for i in com:
            index = list1.index(i) + list2.index(i)
            dict[i] = index
            m = min(index,m)
        L = []
        for key in dict:
            if dict[key] == m:
                L.append(key)
        return L

        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

