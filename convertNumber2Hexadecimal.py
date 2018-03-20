class Solution:
    def toHex(self, num):
        dict = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        s = ''
        if num >= 0:
            pass
        else:
            num = 4294967296 - abs(num)

        d = num // 16
        r = num % 16
        while d != 0:
            if r < 10:
                s += str(r)
            else:
                s += dict[r]

            r = d % 16
            d = d // 16

        if r < 10:
            s += str(r)
        else:
            s += dict[r]

        return s[-1::-1]
