class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # Get coordinates of all 1s in both images
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Count the frequency of each translation vector (offset)
        count = collections.Counter((r1 - r2, c1 - c2) for r1, c1 in ones1 for r2, c2 in ones2)
        
        # Return the max count of any single offset, or 0 if no 1s overlap
        return max(count.values()) if count else 0
