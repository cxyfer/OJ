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
Same as 2406. Divide Intervals Into Minimum Number of Groups
只是本題的區間是 [s, e)，而 2406 是 [s, e]，所以差分或貪心的時候要注意。
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
        intervals.sort(key=lambda x: x[0])
        hp = []
        for left, right in intervals:
            if hp and left >= hp[0]:  # 可以接在堆頂那組的後面
                heapreplace(hp, right)
            else:
                heappush(hp, right)
        return len(hp)


Solution = Solution1
# Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.minMeetingRooms([[0,30],[5,10],[15,20]]))  # 2
print(sol.minMeetingRooms([[7,10],[2,4]]))  # 1
print(sol.minMeetingRooms([[13,15],[1,13]]))  # 1

# @lcpr case=start
# [[0,30],[5,10],[15,20]]\n
# @lcpr case=end

# @lcpr case=start
# [[7,10],[2,4]]\n
# @lcpr case=end