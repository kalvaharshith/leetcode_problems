class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words=s1.split()+s2.split()
        freq={}
        for word in words:
            freq[word]=freq.get(word,0)+1
        res=[]
        for word in freq:
            if freq[word]==1:
                res.append(word)
        return res
        