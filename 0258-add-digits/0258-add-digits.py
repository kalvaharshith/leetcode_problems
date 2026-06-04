class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            curr_sum = 0
            temp = num

            while temp > 0:
                digit = temp % 10
                curr_sum += digit
                temp //= 10

            num = curr_sum

        return num