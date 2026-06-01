#
# @lc app=leetcode id=2406 lang=python3
# @lcpr version=30204
#
# [2406] Divide Intervals Into Minimum Number of Groups
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. 貪心
2. 差分
Same as 253. Meeting Rooms II (Premium)
只是本題的區間是 [s, e]，而 253 是 [s, e)，所以差分或貪心的時候要注意。
"""
# @lc code=start
class Solution1:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        hp = []
        for left, right in intervals:
            if hp and left > hp[0]:  # 可以接在堆頂那組的後面
                heapreplace(hp, right)
            else:
                heappush(hp, right)
        return len(hp)


class Solution2:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for l, r in intervals:
            events.append((l, 1))
            events.append((r + 1, -1))
        events.sort()  # 同一時間點先處理 -1 (結束) 再處理 +1 (開始)

        ans = s = 0
        for _, v in events:
            s += v
            ans = max(ans, s)
        return ans


class Solution3:
    def minGroups(self, intervals: List[List[int]]) -> int:
        diff = defaultdict(int)
        for l, r in intervals:
            diff[l] += 1
            diff[r + 1] -= 1

        ans = s = 0
        for _, v in sorted(diff.items()):
            s += v
            ans = max(ans, s)
        return ans


Solution = Solution1
# Solution = Solution2
# Solution = Solution3
# @lc code=end

sol = Solution()
print(sol.minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))  # 3

#
# @lcpr case=start
# [[5,10],[6,8],[1,5],[2,3],[1,10]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[5,6],[8,10],[11,13]]\n
# @lcpr case=end

#

