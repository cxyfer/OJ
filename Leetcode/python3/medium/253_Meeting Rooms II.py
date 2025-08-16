#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. 差分
2. 貪心
"""
# @lc code=start
class Solution1:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        diff = defaultdict(int)
        for s, e in intervals:
            diff[s] += 1
            diff[e] -= 1
        ans = s = 0
        for _, d in sorted(diff.items()):
            s += d
            ans = max(ans, s)
        return ans

class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key=lambda x: x[0])
        hp = []  # 維護已經開始的會議的結束時間
        for s, e in intervals:
            while hp and hp[0] <= s:  # 去除已經結束的會議
                heappop(hp)
            heappush(hp, e)
            ans = max(ans, len(hp))  # 維護最大會議室數量
        return ans

# Solution = Solution1
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.minMeetingRooms([[0,30],[5,10],[15,20]]))  # 2
print(sol.minMeetingRooms([[7,10],[2,4]]))  # 1


# @lcpr case=start
# [[0,30],[5,10],[15,20]]\n
# @lcpr case=end

# @lcpr case=start
# [[7,10],[2,4]]\n
# @lcpr case=end