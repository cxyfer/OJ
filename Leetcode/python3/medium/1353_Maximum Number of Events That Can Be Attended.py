#
# @lc app=leetcode id=1353 lang=python3
#
# [1353] Maximum Number of Events That Can Be Attended
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def maxEvents(self, events: List[List[int]]) -> int:
        max_ed = max(ed for _, ed in events)
        groups = [[] for _ in range(max_ed + 1)]
        for st, ed in events:
            groups[st].append(ed)
        ans = 0
        hp = []
        for d in range(1, max_ed + 1):
            while hp and hp[0] < d:
                heappop(hp)
            for ed in groups[d]:
                heappush(hp, ed)
            if hp:
                heappop(hp)
                ans += 1
        return ans


class Solution2:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key=lambda x: x[0])
        max_ed = max(ed for _, ed in events)
        ans = i = 0
        cur = events[0][0]
        hp = []
        while cur <= max_ed:
            while hp and hp[0] < cur:
                heappop(hp)
            while i < n and events[i][0] <= cur:
                heappush(hp, events[i][1])
                i += 1
            if hp:
                heappop(hp)
                ans += 1
            if i < n and not hp:
                cur = events[i][0]
            else:
                cur += 1
        return ans


# Solution = Solution1
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.maxEvents([[1,2],[2,3],[3,4]]))  # 3
print(sol.maxEvents([[1,2],[2,3],[3,4],[1,2]]))  # 4
print(sol.maxEvents([[1,2],[1,2],[3,3],[1,5],[1,5]]))  # 5