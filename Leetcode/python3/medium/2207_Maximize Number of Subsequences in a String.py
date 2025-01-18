#
# @lc app=leetcode id=2207 lang=python3
# @lcpr version=30204
#
# [2207] Maximize Number of Subsequences in a String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        n = len(text)
        x, y = pattern
        pre_x = [0] * (n + 1)
        for i, ch in enumerate(text):
            pre_x[i + 1] = pre_x[i] + (ch == x)
        ans = 0
        cnt_y = 0
        for i in range(n):
            if text[i] == y:
                ans += pre_x[i]
                cnt_y += 1
        return ans + max(pre_x[-1], cnt_y)

class Solution2:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        x, y = pattern
        ans = cnt_x = cnt_y = 0
        for ch in text:
            # 先處理 y 是因為可能有 x == y 的情況，因此也不能用 else if
            if ch == y:
                ans += cnt_x
                cnt_y += 1
            if ch == x:
                cnt_x += 1 # prefix sum
        # 最後加上添加一個字元的最大收益，即 max(cnt_x, cnt_y)
        return ans + max(cnt_x, cnt_y)
    
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.maximumSubsequenceCount("abdcdbc", "ac")) # 4
print(sol.maximumSubsequenceCount("aabb", "ab")) # 6
print(sol.maximumSubsequenceCount("fwymvreuftzgrcrxczjacqovduqaiig", "yy")) # 1
#
# @lcpr case=start
# "abdcdbc"\n"ac"\n
# @lcpr case=end

# @lcpr case=start
# "aabb"\n"ab"\n
# @lcpr case=end

#

