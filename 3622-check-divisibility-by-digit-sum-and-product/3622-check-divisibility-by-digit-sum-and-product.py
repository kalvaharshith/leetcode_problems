class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        product=1
        temp=n
        while temp>0:
            digit=temp%10
            s+=digit
            product*=digit
            temp//=10
        if n% (s+product)==0:
            return True
        else:
            return False 