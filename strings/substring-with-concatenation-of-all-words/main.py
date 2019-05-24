class Solution:
    def findSubstring(s, words):
        if s == "" or words == []:
            return []
        res = []

        wordsdict = {}
        tempwordsdict = {}
        for word in words:
            if word in wordsdict:
                wordsdict[word] += 1
            else:
                wordsdict[word] = 1

        wl = len(words[0])
        ll = len(words)
        rl = ll * wl
        for i in range(len(s) - rl + 1):
            temp = s[i:i + rl]
            tempwordsdict.clear()
            for j in range(ll):
                theword = temp[wl * j: wl * (j + 1)]
                if theword not in wordsdict:
                    break
                else:
                    if theword in tempwordsdict:
                        tempwordsdict[theword] += 1
                        if tempwordsdict[theword] > wordsdict[theword]:
                            break
                    else:
                        tempwordsdict[theword] = 1

                if j == ll - 1:
                    res.append(i)
        return res

