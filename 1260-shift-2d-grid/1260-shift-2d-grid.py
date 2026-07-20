class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        arr = []

        # Flatten the grid
        for row in grid:
            arr.extend(row)

        k %= (m * n)

        # Rotate
        arr = arr[-k:] + arr[:-k]

        # Build the answer
        ans = []
        idx = 0
        for i in range(m):
            ans.append(arr[idx:idx+n])
            idx += n

        return ans