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
        nums = list(map(int, s))
        cnt = [0] * 5
        for x in nums:
            cnt[x] += 1

        ans = -inf
        for a in range(5):
            for b in range(5):
                if a == b or cnt[a] == 0 or cnt[b] == 0:
                    continue
                # min(sa[j] - sb[j])，且 (sa_j, sb_j) 的奇偶性分別為 (0, 0), (0, 1), (1, 0), (1, 1)
                min_sl = [inf] * 4
                sa = [0] * (n + 1)
                sb = [0] * (n + 1)
                left = 0
                for i, x in enumerate(nums, start=1):
                    sa[i] = sa[i - 1] + (x == a)
                    sb[i] = sb[i - 1] + (x == b)
                    while i - left >= k and sa[left] < sa[i] and sb[left] < sb[i]:
                        idx = ((sa[left] & 1) << 1) | (sb[left] & 1)
                        min_sl[idx] = min(min_sl[idx], sa[left] - sb[left])
                        left += 1
                    # 因為 a 需要有奇數個，因此 sa[j] 的奇偶性需要與 sa[i] 相反
                    idx = ((sa[i] & 1 ^ 1) << 1) | (sb[i] & 1)
                    ans = max(ans, sa[i] - sb[i] - min_sl[idx])
        return ans  # 題目保證至少有一個合法的子字串
# @lc code=end

sol = Solution()
print(sol.maxDifference("12233", 4))  # -1
print(sol.maxDifference("1122211", 3))  # 1