# @algorithm @lc id=3361 lang=python3 
# @title latest-time-you-can-obtain-after-replacing-characters


from en.Python3.mod.preImport import *
# @test("1?:?4")="11:54"
# @test("0?:5?")="09:59"
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