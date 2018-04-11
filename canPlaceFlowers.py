class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l = len(flowerbed)
        if l == 0:
            return n <= l
        if l == 1:
            if flowerbed[0] == 1:
                return n <= 0
            else:
                return n <= l
        if l == 2:
            if flowerbed == [0, 0]:
                return n <= 1
            else:
                return n <= 0

        sum = 0
        i = 0
        while i < l:
            if i == 0:
                if flowerbed[i:i + 2] == [0, 0]:
                    sum += 1
                    flowerbed[i:i + 2] = [1, 0]
                i += 1
                continue

            if i == l - 1:
                if flowerbed[i - 1:i + 1] == [0, 0]:
                    sum += 1
                    flowerbed[i - 1:i + 1] = [0, 1]
                i += 1
                continue

            if flowerbed[i - 1:i + 2] == [0, 0, 0]:
                sum += 1
                flowerbed[i - 1:i + 2] = [0, 1, 0]

            i += 1

        print(flowerbed)

        return n <= sum










