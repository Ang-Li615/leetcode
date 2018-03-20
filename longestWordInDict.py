class Solution:
    def longestWord(self,words):
        l = len(words)
        print(l)
        if l == 1:
            if len(words[0]) == 1:
                return words[0]
            else:
                return ''
        if l > 1000:
            return False

        dict = {i:len(i) for i in words}
        L = set([len(i) for i in words])
        LL = []
        while LL == []:
            m = max(L)
            if m > 30:
                return False
            for key in words:
                judge = True
                if dict[key] == m:
                    i = m - 1
                    while i > 0:
                        if key[0:i] in dict:
                            i -= 1
                            continue
                        else:
                            judge = False
                            break
                    if judge == True:
                        LL.append(key)
            L.remove(m)

        LL = sorted(LL)
        return LL[0]


