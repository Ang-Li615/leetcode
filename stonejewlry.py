class Solution:
    def numJewelsInStones(self, J, S):
        dict = {s:0 for s in S}
        for s in S:
            dict[s] = dict[s] + 1

        count = 0
        for char in J:
            if char in dict.keys():
                count = count + dict[char]
        return count