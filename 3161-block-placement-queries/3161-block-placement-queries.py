from bisect import bisect_right, insort

class SegmentTree:
    def __init__(self, n):
        self.n = n
        # 4 * n is the standard upper bound for a pointer-based array segment tree
        self.tree = [0] * (4 * n)

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return max(self.query(2 * node, start, mid, l, r), 
                   self.query(2 * node + 1, mid + 1, end, l, r))

class Solution:
    def getResults(self, queries: list[list[int]]) -> list[bool]:
        # Step 1: Find the upper coordinate boundary based on constraints or inputs
        max_x = max(max(q[1] for q in queries), 50000)
        
        # Initialize tree over the safe range [0, max_x + 1]
        st = SegmentTree(max_x + 2)
        
        # Guard rails for tracking adjacent obstacles easily
        obstacles = [0, max_x + 2]
        res = []
        
        for q in queries:
            q_type = q[0]
            x = q[1]
            
            if q_type == 1:
                # Find adjacent obstacles
                idx = bisect_right(obstacles, x)
                prev_obs = obstacles[idx - 1]
                next_obs = obstacles[idx]
                
                # Insert the obstacle to keep list sorted
                insort(obstacles, x)
                
                # Calculate new segmented gap lengths and update Segment Tree
                st.update(1, 0, max_x + 1, x, x - prev_obs)
                st.update(1, 0, max_x + 1, next_obs, next_obs - x)
                
            elif q_type == 2:
                sz = q[2]
                
                # Find the nearest obstacle to the left of (or at) 'x'
                idx = bisect_right(obstacles, x)
                prev_obs = obstacles[idx - 1]
                
                # Query the maximum complete gap anywhere up to x
                max_gap = st.query(1, 0, max_x + 1, 0, x)
                
                # Also check the remaining open gap right before x
                max_gap = max(max_gap, x - prev_obs)
                
                res.append(max_gap >= sz)
                
        return res
