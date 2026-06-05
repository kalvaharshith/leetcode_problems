from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = {}
        duplicate = missing = -1

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for i in range(1, len(nums) + 1):
            if freq.get(i, 0) == 2:
                duplicate = i
            elif freq.get(i, 0) == 0:
                missing = i
        return [duplicate, missing]