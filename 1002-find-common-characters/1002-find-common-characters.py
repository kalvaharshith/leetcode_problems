class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for ch in set(words[0]):
            min_count = min(word.count(ch) for word in words)
            res.extend([ch] * min_count)
        return res


        