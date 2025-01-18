#
# @lc app=leetcode id=1405 lang=python3
# @lcpr version=30204
#
# [1405] Longest Happy String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        hp = [(-a, 'a'), (-b, 'b'), (-c, 'c')] # Max Heap
        heapify(hp)
        ans = ""
        while -hp[0][0] > 0:
            x, ch_x = heappop(hp)
            if len(ans) >= 2 and ans[-1] == ans[-2] == ch_x:
                y, ch_y = heappop(hp)
                if y >= 0:
                    break
                ans += ch_y
                heappush(hp, (y + 1, ch_y))
                heappush(hp, (x, ch_x))
            else:
                ans += ch_x
                heappush(hp, (x + 1, ch_x))
        return ans
# @lc code=end

sol = Solution()
print(sol.longestDiverseString(1, 1, 7))

#
# @lcpr case=start
# 1\n1\n7\n
# @lcpr case=end

# @lcpr case=start
# 7\n1\n0\n
# @lcpr case=end

#

