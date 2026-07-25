#
# @lc app=leetcode id=3992 lang=python3
#
# [3992] Rearrange String to Avoid Character Pair
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. 先統計每個字元的數量，將 y 與 x 放在最前面，其他字元放在後面即可。
2. 也可以使用 3-Way QuickSort 將 y 排在最前面，x 排在最後面，其他字元排在中間。
   同 75. Sort Colors 。
"""
# @lc code=start
class Solution1:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        cnt = Counter(s)
        ans = [y * cnt[y], x * cnt[x]]
        for c, v in cnt.items():
            if c != x and c != y:
                ans.append(c * v)
        return "".join(ans)


class Solution2:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        n = len(s)
        s = list(s)
        # 3-Way QuickSort, same as 75. Sort Colors
        i, l, r = 0, 0, n - 1
        while i <= r:
            if s[i] == y:
                s[i], s[l] = s[l], s[i]
                l += 1
                i += 1
            elif s[i] == x:
                s[i], s[r] = s[r], s[i]
                r -= 1
            else:
                i += 1
        return "".join(s)


# Solution = Solution1
Solution = Solution2
# @lc code=end
