class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        sub=[]
        def solve(i,curr):
            if i==len(nums):
                sub.append(curr.copy())
                return
            curr.append(nums[i])
            solve(i+1,curr)
            curr.pop()
            solve(i+1,curr)
        solve(0,[])
        return sub

        