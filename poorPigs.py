class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        n = minutesToTest / minutesToDie + 1
        m = 1
        sum = 0
        while True:
            m = m * n
            sum += 1
            if m >= buckets:
                return sum