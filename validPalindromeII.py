class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        i = 0
        j = l - 1
        times = 0
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                times += 1
                break

        if times == 0:
            return True

        if i == j - 1:
            return True

        i1 = i
        j1 = j - 1
        while i1 < j1:
            if s[i1] == s[j1]:
                i1 += 1
                j1 -= 1
            else:
                times += 1
                break

        if times == 1:
            return True

        i1 = i + 1
        j1 = j
        times = 1
        while i1 < j1:
            if s[i1] == s[j1]:
                i1 += 1
                j1 -= 1
            else:
                times += 1
                break

        if times == 1:
            return True

        return False




















                if i == j - 1 and times == 0:
                    return True
                elif i < j - 1:
                    if s[i] == s[j-1]:
                        times += 1
                        i += 1
                        j -= 2
                    elif s[i+1] == s[j]:
                        times += 1
                        i += 2
                        j -= 1
                    else:
                        return False
        return True


