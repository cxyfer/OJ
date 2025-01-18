#
# @lc app=leetcode id=3170 lang=python3
# @lcpr version=30203
#
# [3170] Lexicographically Minimum String After Removing Stars
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. 常規作法，每次都遍歷 26 個字母，找到最小字母的最後一個位置，然後刪除
        2. 用 heap 來保存所有字母的位置，每次刪除最小字母的最後一個位置

        由於 Python 不能直接修改字串，因此這裡是另外創建一個 list 來重建字串
    """
    def clearStars(self, s: str) -> str:
        # return self.solve1(s)
        return self.solve2(s)
    def solve1(self, s: str) -> str:
        n = len(s)
        pos = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            idx = ord(ch) - ord("a")
            if ch != "*":
                pos[idx].append(i)
            else:
                for i in range(26):
                    if pos[i]:
                        pos[i].pop()
                        break
        ans = [""] * n
        for i in range(26):
            for j in pos[i]:
                ans[j] = chr(i + ord("a"))
        return "".join(ans)
    def solve2(self, s: str) -> str:
        n = len(s)
        hp = []
        for i, ch in enumerate(s):
            c = ord(ch) - ord("a")
            if ch != "*":
                heappush(hp, (c, -i))
            else:
                heappop(hp)
        ans = [""] * n
        while hp:
            c, i = heappop(hp)
            ans[-i] = chr(c + ord("a"))
        return "".join(ans)
# @lc code=end



#
# @lcpr case=start
# "aaba*"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n
# @lcpr case=end

#

