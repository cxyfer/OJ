#
# @lc app=leetcode id=2597 lang=python3
# @lcpr version=30202
#
# [2597] The Number of Beautiful Subsets
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. 回溯 + 剪枝
        2. 動態規劃
    """
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # return self.solve1a(nums, k)
        # return self.solve1b(nums, k)
        return self.solve2(nums, k)
    def solve1a(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0 # 去除空集合
        cnt = Counter()
        # cnt = [0] * (max(nums) + 2 * k + 1)
        def dfs(i: int) -> None: # 第一種：選或不選
            nonlocal ans
            if i == n:
                ans += 1
                return
            dfs(i + 1) # 不選
            x = nums[i]
            if cnt[x-k] == 0 and cnt[x+k] == 0: # 滿足條件
                cnt[x] += 1
                dfs(i + 1) # 選
                cnt[x] -= 1
        dfs(0)
        return ans - 1 # 去除空集合
    def solve1b(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cnt = Counter()
        # cnt = [0] * (max(nums) + 2 * k + 1)
        def dfs(i: int) -> None: # 第二種：枚舉下一個選哪個
            nonlocal ans
            ans += 1
            for j in range(i, n): # 枚舉下一個選的是哪個
                x = nums[j]
                if cnt[x-k] == 0 and cnt[x+k] == 0: # 滿足條件
                    cnt[x] += 1
                    dfs(j + 1)
                    cnt[x] -= 1
        dfs(0)
        return ans - 1 # 去除空集合
    def solve2(self, nums: List[int], k: int) -> int:
        groups = defaultdict(Counter)
        # groups = [Counter() for _ in range(k)]
        for x in nums:
            groups[x % k][x] += 1
        ans = 1
        for _, cnt in groups.items():
        # for cnt in groups:
        #     if not cnt: continue
            m = len(cnt)
            keys = sorted(cnt.keys())
            dp = [0] * (m + 1) # dp[i] 表示前 i 個數字的方案數，1-indexed
            dp[0], dp[1] = 1, 1 << cnt[keys[0]] # 初始化 dp[1] 為 不選和選第一個
            for i in range(1, m):
                # x = keys[i] 的數量有 cnt[x] 個 選 x 的方案有 2^cnt[x] -1 種，不選 x 的方案有 1 種
                x = keys[i]
                if keys[i] - keys[i-1] == k: # 和前一個相差為 k ，則不能同時選 keys[i] 和 keys[i-1]
                    dp[i+1] = dp[i] + dp[i-1] * ((1 << cnt[x]) - 1)
                else:
                    dp[i+1] = dp[i] << cnt[x]
            ans *= dp[m] # 乘法原理
        return ans - 1 # 去除空集合
# @lc code=end

sol = Solution()
print(sol.beautifulSubsets([2,4,6], 2))

#
# @lcpr case=start
# [2,4,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

