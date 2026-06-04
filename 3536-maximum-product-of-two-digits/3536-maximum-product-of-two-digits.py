class Solution:
    def maxProduct(self, n: int) -> int:
        na = []

        while n > 0:
            digit = n % 10
            na.append(digit)
            n //= 10

        max1 = max(na)
        na.remove(max1)
        max2 = max(na)

        return max1 * max2
        

        