#
# @lc app=leetcode id=2406 lang=python3
# @lcpr version=30204
#
# [2406] Divide Intervals Into Minimum Number of Groups
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
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
        diff = SortedDict()
        for l, r in intervals:
            diff[l] = diff.get(l, 0) + 1
            diff[r + 1] = diff.get(r + 1, 0) - 1

        ans = s = 0
        for v in diff.values():
            s += v
            ans = max(ans, s)
        return ans


# Solution = Solution1
Solution = Solution2
# @lc code=end



#
# @lcpr case=start
# [[5,10],[6,8],[1,5],[2,3],[1,10]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[5,6],[8,10],[11,13]]\n
# @lcpr case=end

#

