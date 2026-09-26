class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=1
        h=num
        while l<=h:
            mid=l+(h-l)//2
            sq=mid*mid
            if sq==num:
                return True
            elif sq<num:
                l=mid+1
            else:
                h=mid-1
        return False
