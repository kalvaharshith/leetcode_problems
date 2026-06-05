class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq={}
        for num in arr1:
            freq[num]=freq.get(num,0)+1
        res=[]
        for num in arr2:
            res.extend([num]*freq[num])
            del freq[num]
        for num in sorted(freq):
             res.extend([num]*freq[num])
        return res


        