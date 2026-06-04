class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        curr_sum=0
        d_sum=0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            digit=nums[i]
            while digit>0:
                d_sum+=digit%10
                digit//=10
        return abs(curr_sum-d_sum)