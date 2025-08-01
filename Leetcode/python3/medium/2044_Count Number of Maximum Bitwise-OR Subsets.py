#
# @lc app=leetcode id=2044 lang=python3
# @lcpr version=30204
#
# [2044] Count Number of Maximum Bitwise-OR Subsets
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. 枚舉子集: O(n * 2^n)
2. 回溯: O(2^n)
3. Top-Down DP: O(2^n)
4. Bottom-Up DP: O(n * 2^n) / O(2^n)
"""
# @lc code=start
class Solution1:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        mx = reduce(or_, nums)
        ans = 0
        for s in range(1, 1 << n): # 枚舉所有子集
            cur = 0
            for i in range(n):
                if (s >> i) & 1:
                    cur |= nums[i]
            if cur == mx:
                ans += 1
        return ans
    
class Solution2:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = mx = 0
        def dfs(i, cur):
            nonlocal ans, mx
            if i == len(nums):
                if cur == mx:
                    ans += 1
                elif cur > mx:
                    mx = cur
                    ans = 1
                return
            dfs(i + 1, cur | nums[i])
            dfs(i + 1, cur)
        dfs(0, 0)
        return ans
    
class Solution3:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        mx = reduce(or_, nums)
        @cache  # Memoization
        def dfs(i, cur):
            if i == n:
                return cur == mx
            return dfs(i + 1, cur) + dfs(i + 1, cur | nums[i])  # 選或不選
        return dfs(0, 0)
    
class Solution4a:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = reduce(or_, nums)
        # f[i] 表示子集的 OR 值為 i 的子集數量
        f = [0] * (1 << mx.bit_length())
        f[0] = 1
        for x in nums:
            for i in range(mx, -1, -1):
                f[i | x] += f[i]
        return f[mx]
    
class Solution4b:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = reduce(or_, nums)
        f = defaultdict(int)
        f[0] = 1
        for x in nums:
            nf = f.copy()
            for y in f:
                nf[y | x] += f[y]
            f = nf
        return f[mx]

# Solution = Solution1
# Solution = Solution2
# Solution = Solution3
# Solution = Solution4a
Solution = Solution4b
# @lc code=end

sol = Solution()
print(sol.countMaxOrSubsets([3,1]))
print(sol.countMaxOrSubsets([1 << b for b in range(1, 17)]))

#
# @lcpr case=start
# [3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,5]\n
# @lcpr case=end

#

