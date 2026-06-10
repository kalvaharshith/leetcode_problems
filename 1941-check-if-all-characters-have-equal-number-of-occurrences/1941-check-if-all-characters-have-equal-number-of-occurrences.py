class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        values=list(freq.values())
        for count in values:
            if count !=values[0]:
                return False
        return True
        