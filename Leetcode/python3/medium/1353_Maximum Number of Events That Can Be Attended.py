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
    
class Solution2:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key=lambda x: x[0])
        mx_ed = max(e for _, e in events)
        ans = 0
        i = 0
        cur = events[0][0]
        hp = []
        while cur <= mx_ed:
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

Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.maxEvents([[1,2],[2,3],[3,4]]))  # 3
print(sol.maxEvents([[1,2],[2,3],[3,4],[1,2]]))  # 4
print(sol.maxEvents([[1,2],[1,2],[3,3],[1,5],[1,5]]))  # 5