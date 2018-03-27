class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """



        s = list(s)
        vowels = ['a','e','i','o','u']
        pointer1 = 0
        pointer2 = len(s) - 1

        while pointer1 < pointer2:
            if s[pointer1] in vowels and s[pointer2] in vowels:
                s[pointer1],s[pointer2] = s[pointer2],s[pointer1]
                pointer1 += 1
                pointer2 -= 1
            elif s[pointer1] in vowels and s[pointer2] not in vowels:
                pointer2 -= 1
            elif s[pointer1] not in vowels and s[pointer2] in vowels:
                pointer1 += 1
            else:
                pointer1 += 1
                pointer2 -= 1

        return ''.join(s)