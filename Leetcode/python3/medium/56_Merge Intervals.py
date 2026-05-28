#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda p: p[0])  # sort by left endpoint
        for l, r in intervals:
            if not ans or l > ans[-1][1]:  # not overlap
                ans.append([l, r])
            else:
                ans[-1][1] = max(ans[-1][1], r)  # overlap, update interval
        return ans


class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mx = max(r for _, r in intervals)

        diff = [0] * (mx * 2 + 2)
        for l, r in intervals:
            diff[l * 2] += 1
            diff[r * 2 + 1] -= 1

        ans = []
        s = 0
        st = -1
        for i, d in enumerate(diff):
            s += d
            if s > 0:
                if st < 0:  # 開始一個新的區間
                    st = i
            elif st >= 0:
                ans.append([st // 2, i // 2])
                st = -1
        return ans


# Solution = Solution1
Solution = Solution2
# @lc code=end