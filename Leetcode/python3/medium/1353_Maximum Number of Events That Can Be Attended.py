#
# @lc app=leetcode id=1353 lang=python3
#
# [1353] Maximum Number of Events That Can Be Attended
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        mp = defaultdict(list)
        for s, e in events:
            mp[s].append(e)
        ans = 0
        hp = []
        for i in range(1, max(e for _, e in events) + 1):
            while hp and hp[0] < i:
                heappop(hp)
            if i in mp:
                for e in mp[i]:
                    heappush(hp, e)
            if hp:
                heappop(hp)
                ans += 1
        return ans
# @lc code=end

