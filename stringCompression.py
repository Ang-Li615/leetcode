class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        t = chars[0]
        pointer2 = 0
        count = 0
        for e in chars:
            if e == t:
                count += 1
            else:
                chars[pointer2] = t
                pointer2 += 1
                if count != 1:
                    for n in str(count):
                        chars[pointer2] = n
                        pointer2 += 1
                count = 1
                t = e
        chars[pointer2] = t
        pointer2 += 1
        if count != 1:
            for n in str(count):
                chars[pointer2] = n
                pointer2 += 1
        return pointer2