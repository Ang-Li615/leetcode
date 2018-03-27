class Solution:
    def plusOne(self, digits):
        self.L = []
        l = len(digits)
        i = l - 1
        self.carry = 1
        self.carrybit(digits,i,self.carry)
        return self.L[-1::-1]



    def carrybit(self,digits,i,carry):
        if i == -1:
            if carry == 1:
                self.L.append(1)
                return None
            else:
                return None

        if digits[i] + carry == 10:
            self.L.append(0)
            carry = 1
        else:
            self.L.append(digits[i] + 1)
            carry = 0
        self.carrybit(digits,i-1,carry)

