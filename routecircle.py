class Solution:
    def judgeCircle(self, moves):
        dict = {i:0 for i in 'UDLR'}
        for i in moves:
            dict[i] = dict[i] + 1

        if dict['U'] == dict['D'] and dict['L'] == dict['R']:
            return True
        else:
            return False

