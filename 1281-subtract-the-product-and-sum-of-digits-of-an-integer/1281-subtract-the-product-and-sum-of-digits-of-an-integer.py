class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro=1
        su=0
        while n>0:
            digit=n%10
            pro*=digit
            su+=digit
            n //= 10
        return pro - su