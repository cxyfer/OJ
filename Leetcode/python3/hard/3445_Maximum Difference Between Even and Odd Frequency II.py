#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#


# @lcpr-template-start
from preImport import *
import string
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        ans = float('-inf')
        cnt = Counter(s)
        for a in string.digits:
            for b in string.digits:
                if a == b or cnt[a] == 0 or cnt[b] == 0:
                    continue
                sa = [0] * (n + 1)
                sb = [0] * (n + 1)
                # (sa_j - sb_j) 的最小值，且 (sa_j, sb_j) 的奇偶性分別為 (0, 0), (0, 1), (1, 0), (1, 1)
                mns = [float('inf'), float('inf'), float('inf'), float('inf')]  # (0, 0), (0, 1), (1, 0), (1, 1)
                left = 0
                for i, d in enumerate(s, 1):
                    sa[i] = sa[i - 1] + (d == a)
                    sb[i] = sb[i - 1] + (d == b)
                    while left <= i - k and sa[left] != sa[i] and sb[left] != sb[i]:
                        idx = ((sa[left] & 1) << 1) | (sb[left] & 1)
                        mns[idx] = min(mns[idx], sa[left] - sb[left])
                        left += 1
                    idx = (((sa[i] & 1) ^ 1) << 1) | (sb[i] & 1)
                    ans = max(ans, sa[i] - sb[i] - mns[idx])
        return ans
# @lc code=end

sol = Solution()
# print(sol.maxDifference("12233", 4))  # -1
print(sol.maxDifference("1122211", 3))  # 1