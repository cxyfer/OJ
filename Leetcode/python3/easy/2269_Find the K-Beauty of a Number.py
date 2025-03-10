#
# @lc app=leetcode.cn id=2269 lang=python3
# @lcpr version=30204
#
# [2269] 找到一个数字的 K 美丽值
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        ans = 0
        for i in range(n - k + 1):
            x = int(s[i:i+k])
            ans += (x and num % x == 0)
        return ans

class Solution2:
    def divisorSubstrings(self, num: int, k: int) -> int:
        base = pow(10, k)
        ans = 0
        t = num
        while t >= base // 10: # 要多一次
            x = t % base
            ans += (x and num % x == 0)
            t //= 10
        return ans

class Solution(Solution1):
# class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.divisorSubstrings(240, 2))  # 2
print(sol.divisorSubstrings(430043, 2))  # 2

#
# @lcpr case=start
# 240\n2\n
# @lcpr case=end

# @lcpr case=start
# 430043\n2\n
# @lcpr case=end

#

