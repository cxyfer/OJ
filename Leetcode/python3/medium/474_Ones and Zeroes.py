#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1a:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            cnt0 = s.count('0')
            cnt1 = len(s) - cnt0
            for i in range(m, cnt0 - 1, -1):
                for j in range(n, cnt1 - 1, -1):
                    v = f[i - cnt0][j - cnt1] + 1
                    if v > f[i][j]:
                        f[i][j] = v
        return f[m][n]

class Solution1b:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        f = [[0] * (n + 1) for _ in range(m + 1)]
        mx0 = mx1 = 0
        for s in strs:
            cnt0 = s.count('0')
            cnt1 = len(s) - cnt0
            mx0 = min(mx0 + cnt0, m)
            mx1 = min(mx1 + cnt1, n)
            for i in range(mx0, cnt0 - 1, -1):
                for j in range(mx1, cnt1 - 1, -1):
                    v = f[i - cnt0][j - cnt1] + 1
                    if v > f[i][j]:
                        f[i][j] = v
        return max(map(max, f))

# Solution = Solution1a
Solution = Solution1b
# @lc code=end

sol = Solution()
print(sol.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))  # 4
print(sol.findMaxForm(["10","0001","111001","1","0"], 3, 4))  # 3
