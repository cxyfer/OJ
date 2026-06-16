#
# @lc app=leetcode id=3614 lang=python3
#
# [3614] Process String with Special Operations II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lengths = []
        ln = 0
        for ch in s:
            if ch == '*':
                ln = max(ln - 1, 0)
            elif ch == '#':
                ln *= 2
            elif ch == '%':
                pass
            else:
                ln += 1
            lengths.append(ln)

        if k >= lengths[-1]:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]
            ln = lengths[i]
            if ch == '*':
                continue
            elif ch == '#':
                if k >= ln // 2:  # k 在後半部分
                    k -= ln // 2
            elif ch == '%':  # 翻轉前的 ln - 1 - k 就是翻轉後的 k
                k = ln - 1 - k
            elif k == ln - 1:  # k 就是當前字母
                return ch

        return '.'
# @lc code=end

