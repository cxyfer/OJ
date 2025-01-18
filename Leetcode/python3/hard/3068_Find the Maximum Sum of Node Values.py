#
# @lc app=leetcode id=3068 lang=python3
# @lcpr version=30202
#
# [3068] Find the Maximum Sum of Node Values
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        x ^ k ^ k = x
        1. 樹形DP
          令 f[u][0/1] 表示 u 操作偶數/奇數次時，其子樹(包括 u)的最大值
          初始化 f[u][0] = 0, f[u][1] = -inf ，後者之所以為 -inf 是因為一開始不考慮任何邊時， u 無法被操作，能操作的情況下都必須比 -inf 大。
        2a. 線性DP
          對於樹上的任兩點u, v，由於樹上兩點間存在一條路徑，故其實可以任選兩點操作，不用建圖。
          令 dp[i][0/1] 表示前 i 個點操作偶數/奇數次時的最大值。
          - 前 i 個點操作偶數次，可以從前 i-1 個點操作偶數次且當前點不操作，或者前 i-1 個點操作奇數次且當前點操作，兩者取最大值。
            即 dp[i][0] = max(dp[i-1][0] + nums[i], dp[i-1][1] + (nums[i] ^ k)) 
          - 前 i 個點操作奇數次，可以從前 i-1 個點操作奇數次且當前點不操作，或者前 i-1 個點操作偶數次且當前點操作，兩者取最大值。
            即 dp[i][1] = max(dp[i-1][1] + nums[i], dp[i-1][0] + (nums[i] ^ k))
          由於總操作一定發生了偶數次，因此最終答案為 dp[n][0] 
        2b. 線性DP空間優化
          由於轉移只和前一個狀態有關，故可以優化空間為 O(1)。
    """
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        return self.solve1(nums, k, edges)
        # return self.solve2a(nums, k, edges)
        # return self.solve2b(nums, k, edges)
    def solve1(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        g = [[] for _ in range(n)] # adjacency list
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        def dfs(u: int, fa: int) -> Tuple[int, int]:
            f0, f1 = 0, -float('inf') # f0/f1: 在 u 操作偶數/奇數次時，其子樹(不包括 u)的最大值，即 f(u, 0) 和 f(u, 1)
            for v in g[u]:
                if v == fa: continue
                r0, r1 = dfs(v, u) # 不操作/操作 (v, u) 這條邊時，v 的子樹(包含 v) 的最大值
                # f0, f1 = max(f0 + r0, f1 + r1), max(f0 + r1, f1 + r0) # 等於以下三行
                t0, t1 = f0, f1 # backup
                f0 = max(t0 + r0, t1 + r1) # 不操作/操作 (u, v) 這條邊
                f1 = max(t0 + r1, t1 + r0) # 不操作/操作 (u, v) 這條邊
            return max(f0 + nums[u], f1 + (nums[u] ^ k)), max(f1 + nums[u], f0 + (nums[u] ^ k)) # 不操作/操作 (u, fa) 這條邊
        return dfs(0, -1)[0]
    def solve2a(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        dp = [[0, -float("inf")] for _ in range(n + 1)] # dp[i][0/1]: 前 i 個點總共操作偶數/奇數次時的最大值
        for i, x in enumerate(nums):
            dp[i+1][0] = max(dp[i][0] + x, dp[i][1] + (x ^ k)) # 當前點不操作/操作
            dp[i+1][1] = max(dp[i][1] + x, dp[i][0] + (x ^ k)) # 當前點不操作/操作
        return dp[n][0]
    def solve2b(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        f0, f1 = 0, -float('inf') # f0/f1: 總共操作偶數/奇數次時的最大值
        for x in nums:
            f0, f1 = max(f0 + x, f1 + (x ^ k)), max(f1 + x, f0 + (x ^ k)) # 不操作/操作
        return f0
# @lc code=end



#
# @lcpr case=start
# [1,2,1]\n3\n[[0,1],[0,2]]\n
# @lcpr case=end

# @lcpr case=start
# [2,3]\n7\n[[0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,7,7]\n3\n[[0,1],[0,2],[0,3],[0,4],[0,5]]\n
# @lcpr case=end

#

