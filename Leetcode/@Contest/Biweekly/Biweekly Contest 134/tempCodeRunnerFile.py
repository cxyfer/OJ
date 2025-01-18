class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        pre = [0] * (2 * n + 1)
        for i in range(2 * n):
            pre[i + 1] = pre[i] + (colors[i % n] != colors[(i-1) % n])
        ans = 0
        for i in range(n):
            if pre[i + k - 1] - pre[i] == k - 1:
                ans += 1
        return ans