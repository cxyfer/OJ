#
# @lc app=leetcode id=3170 lang=python3
# @lcpr version=30203
#
# [3170] Lexicographically Minimum String After Removing Stars
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. 26 個 Stack 來保存所有字母的位置，每次遇到 * 刪除最小字母的最後一個位置
    O(Σn)
2. 用 heap 來保存所有字母的位置，每次刪除最小字母的最後一個位置
    O(n log n)
3. 和 1 相同，但改用 bitmask 來紀錄哪些 Stack 非空
    O(n)
"""
# @lc code=start
class Solution1:
    def clearStars(self, s: str) -> str:
        ans = list(s)
        pos = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            if ch == "*":
                ans[i] = ""
                for c in range(26):
                    if pos[c]:
                        ans[pos[c].pop()] = ""
                        break
            else:
                pos[ord(ch) - ord("a")].append(i)
        return "".join(ans)

class Solution2:
    def clearStars(self, s: str) -> str:
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

class Solution3:
    def clearStars(self, s: str) -> str:
        ans = list(s)
        pos = [[] for _ in range(26)]
        vis = 0
        for i, ch in enumerate(s):
            if ch == "*":
                ans[i] = ""
                lb = vis & -vis
                c = lb.bit_length() - 1
                ans[pos[c].pop()] = ""
                if not pos[c]:
                    vis &= ~(1 << c)
            else:
                c = ord(ch) - ord("a")
                pos[c].append(i)
                vis |= 1 << c
        return "".join(ans)

# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end



#
# @lcpr case=start
# "aaba*"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n
# @lcpr case=end

#

