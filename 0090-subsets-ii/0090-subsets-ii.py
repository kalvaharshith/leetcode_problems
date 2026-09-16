class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        sub=[]
        def solve(i,curr):
            sub.append(curr.copy())
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                curr.append(nums[j])
                solve(j+1,curr)
                curr.pop()
        solve(0,[])
        return sub
