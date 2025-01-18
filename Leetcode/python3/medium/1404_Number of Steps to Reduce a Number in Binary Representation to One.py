#
# @lc app=leetcode id=1404 lang=python3
# @lcpr version=30202
#
# [1404] Number of Steps to Reduce a Number in Binary Representation to One
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numSteps(self, s: str) -> int:
        # return self.solve2a(s)
        return self.solve2b(s)
    def solve2a(self, s: str) -> int:
        n = len(s)
        ans = 0
        flag = False
        for i in range(n-1, -1, -1):
            if s[i] == "0":
                ans += 2 if flag else 1
            else:
                if not flag:
                    ans += 2 if i != 0 else 0
                    flag = True
                else:
                    ans += 1
        return ans
    """
        考慮 0 和 1 的貢獻
        由右向左遍歷，最後一段 0 的的貢獻皆為 1，其餘 0 的貢獻為 2；
        而 1 的貢獻為 1 ，但第一個遇到的 1 的貢獻為 2。
        此外還需考慮一種特殊情況，只有 s[0] == "1" ，其餘位皆為 0 時，此時不用考慮這個 1 的貢獻，直接返回 n-1 即可。
    """
    def solve2b(self, s: str) -> int:
        n = len(s)
        i = n - 1
        while s[i] == "0": # 題目確保 s[0] == "1" ，不用寫 i > 0 
            i -= 1
        return n + s.count("0") - (n-i-1) + 1 if i != 0 else n - 1
# @lc code=end

sol = Solution()
print(sol.numSteps("1101")) # 6
print(sol.numSteps("10")) # 1
print(sol.numSteps("1")) # 0

#
# @lcpr case=start
# "1101"\n
# @lcpr case=end

# @lcpr case=start
# "10"\n
# @lcpr case=end

# @lcpr case=start
# "1"\n
# @lcpr case=end

#

