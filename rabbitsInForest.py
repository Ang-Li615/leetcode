class Solution:
    def numRabbits(slef, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        dict = {i: 0 for i in answers}
        for i in answers:
            dict[i] += 1

        count = 0
        for i in dict:
            quotient = dict[i] // (i+1)
            remainder = dict[i] % (i+1)
            if remainder == 0:
                count += quotient*(i+1)
            else:
                count += quotient*(i+1) + (i+1)

        return count

answers = [0,0,0,1,1]
count = numRabbits(answers)
print(count)
