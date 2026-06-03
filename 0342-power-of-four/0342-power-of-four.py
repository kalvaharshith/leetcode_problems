class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        x=0
        while 4 ** x <= n:
            if 4 ** x == n:
                return True
            x += 1
        return False

