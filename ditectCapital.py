class Solution:
    def detectCapitalUse(self, word):
        correct = False
        if word[0] == word[0].upper():
            if word[1::] == word[1::].upper():
                correct = True
            elif word[1::] == word[1::].lower():
                correct = True



        else:
            if word[1::] == word[1::].lower():
                correct = True


        return correct



