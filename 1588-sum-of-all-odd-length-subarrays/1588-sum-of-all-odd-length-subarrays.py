class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s=0
        for i in range(len(arr)):
            curr_s=0
            for j in range(i,len(arr)):
                curr_s+=arr[j]
                if(i -j+1)%2==1:
                    s+=curr_s
        return s

        