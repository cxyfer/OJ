#
# @lc app=leetcode id=3169 lang=python3
# @lcpr version=30203
#
# [3169] Count Days Without Meetings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Merge Intervals
    - Similar to 56. Merge Intervals
2. Prefix Sum + Line Sweep
"""
# @lc code=start
class Solution1a:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        merged = [meetings[0]]
        for x, y in meetings:
            if x > merged[-1][1]:
                merged.append([x, y])
            else:
                merged[-1][1] = max(merged[-1][1], y)
        ans = days
        for x, y in merged:
            ans -= y - x + 1  # [x, y] is invalid
        return ans

class Solution1b:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        ans = days
        st, ed = meetings[0]
        for x, y in meetings:
            if x > ed:
                ans -= (ed - st + 1)  # [st, ed] is invalid
                st, ed = x, y
            else:
                ed = max(ed, y)
        ans -= (ed - st + 1)  # [st, ed] is invalid
        return ans
class Solution1c:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        ans = ed = 0
        for x, y in meetings:
            if x > ed:
                ans += x - ed - 1  # [ed + 1, x - 1] is valid
                ed = y
            else:
                ed = max(ed, y)
        ans += days - ed  # [ed + 1, days] is valid
        return ans

class Solution2:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        mp = defaultdict(int)
        for x, y in meetings:
            mp[x] += 1
            mp[y + 1] -= 1
        ans = s = 0
        pre = 1
        for d in sorted(mp.keys()):
            if s == 0:
                ans += d - pre  # [pre, d - 1] is valid
            s += mp[d]
            pre = d
        ans += days - pre + 1  # [pre, days] is valid
        return ans
    
# Solution = Solution1a
# Solution = Solution1b
# Solution = Solution1c
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.countDays(10, [[5,7],[1,3],[9,10]]))  # 2
print(sol.countDays(5, [[2,4],[1,3]]))  # 1
print(sol.countDays(6, [[1,6]]))  # 0
print(sol.countDays(8, [[3,4],[4,8],[2,5],[3,8]]))  # 1
#
# @lcpr case=start
# 10\n[[5,7],[1,3],[9,10]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[2,4],[1,3]]\n
# @lcpr case=end

# @lcpr case=start
# 6\n[[1,6]]\n
# @lcpr case=end

#

