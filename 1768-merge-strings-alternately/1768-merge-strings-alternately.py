class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        mini = min(len(word1), len(word2))
        for i in range(mini):
            res+=word1[i]
            res+=word2[i]
        res+=word1[mini:]
        res+=word2[mini:]
           

        return res