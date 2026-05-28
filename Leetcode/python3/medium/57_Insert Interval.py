#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Greedy + Sorting 
把 newInterval 加入 intervals 後，就是 56. Merge Intervals
Time: O(nlogn)

2. 差分陣列
即 56. Merge Intervals 的差分陣列解法

3. 分類討論
因為給定的 intervals 是無重疊的，因此當發生重疊的情況一定是和 newInterval 重疊
所以可以根據 [li, ri] 和 newInterval 的位置關係分類討論
Time: O(n)
"""
# @lc code=start
class Solution1:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:  # fmt: skip
        ans = []
        intervals.append(newInterval)
        intervals.sort(key=lambda p: p[0])  # sort by left endpoint
        for l, r in intervals:
            if not ans or l > ans[-1][1]:  # not overlap
                ans.append([l, r])
            else:
                ans[-1][1] = max(ans[-1][1], r)  # overlap, update interval
        return ans


class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:  # fmt: skip
        intervals.append(newInterval)
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


class Solution3:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:  # fmt: skip
        left, right = newInterval
        added = False
        ans = []
        for li, ri in intervals:
            # Case 1. 原本的區間完全在 newInterval 的左側
            if ri < left:
                ans.append([li, ri])
            # Case 2. 原本的區間完全在 newInterval 的右側
            elif li > right:
                if not added:
                    ans.append([left, right])
                    added = True
                ans.append([li, ri])
            # Case 3. 與 newInterval 有交集，合併兩者，更新 newInterval 的區間
            else:
                left = min(left, li)
                right = max(right, ri)
        # 考慮沒有任何區間在 newInterval 的右側的情況，此時 newInterval 仍未加入答案中
        if not added:
            ans.append([left, right])
        return ans


# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end

