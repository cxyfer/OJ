#
# @lc app=leetcode id=3771 lang=python3
#
# [3771] Total Score of Dungeon Runs
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Q3. 枚舉右維護左
對於每個 r ，可以計算有多少個 s[l - 1] 可以使 hp - (s[r] - s[l - 1]) >= req[r]
移項得 s[l - 1] >= s[r] + req[r] - hp，使用有序容器維護 s[l - 1] ，每次二分查找即可
"""
# @lc code=start
class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        ans = s = 0
        sl = SortedList([0])  # 保存 s[l - 1]
        for x, y in zip(damage, requirement):
            s += x
            ans += len(sl) - sl.bisect_left(s + y - hp)
            sl.add(s)
        return ans
# @lc code=end

