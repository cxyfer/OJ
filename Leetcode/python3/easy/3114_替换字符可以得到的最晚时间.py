#
# @lc app=leetcode.cn id=3114 lang=python3
#
# [3114] 替换字符可以得到的最晚时间
#

# @lc code=start
class Solution:
    def findLatestTime(self, s: str) -> str:
        # return self.solve1(s)
        return self.solve2(s)
    """
        1. 直接枚舉
    """
    def solve1(self, s: str) -> str:
        for h in range(11, -1, -1):
            for m in range(59, -1, -1):
                t = f"{h:02d}:{m:02d}"
                if all(x == "?" or x == y for x, y in zip(s, t)):
                    return t
    """
        2. 逐位判斷
    """
    def solve2(self, s: str) -> str:
        s = list(s)
        if s[0] == "?":
            s[0] = "1" if s[1] == "?" or s[1] <= "1" else "0"
        if s[1] == "?":
            s[1] = "1" if s[0] == "1" else "9"
        if s[3] == "?":
            s[3] = "5"
        if s[4] == "?":
            s[4] = "9"
        return "".join(s)
# @lc code=end

