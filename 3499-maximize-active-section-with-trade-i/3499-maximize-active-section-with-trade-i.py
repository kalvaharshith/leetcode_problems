class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Find the lengths of all contiguous blocks of '0's
        zero_blocks = []
        current_zeros = 0
        
        for char in s:
            if char == '0':
                current_zeros += 1
            else:
                if current_zeros > 0:
                    zero_blocks.append(current_zeros)
                    current_zeros = 0
        if current_zeros > 0:
            zero_blocks.append(current_zeros)
            
        # If there are fewer than 2 zero segments, max flip gain is 0
        if len(zero_blocks) < 2:
            return s.count('1')
        
        # Calculate maximum sum of any two adjacent zero blocks
        max_zero_merge = 0
        for i in range(len(zero_blocks) - 1):
            max_zero_merge = max(max_zero_merge, zero_blocks[i] + zero_blocks[i + 1])
            
        # The result is total '1's plus the maximal zero block merge
        return s.count('1') + max_zero_merge
