class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s = str(n)
        d = str(x)

        return d in s and s[0] != d