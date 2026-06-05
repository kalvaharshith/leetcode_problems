class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}
        for i in range(1, n + 1):
            s = 0
            temp = i
            while temp:
                s += temp % 10
                temp //= 10
            groups[s] = groups.get(s, 0) + 1
        mx = max(groups.values())
        return sum(1 for v in groups.values() if v == mx)