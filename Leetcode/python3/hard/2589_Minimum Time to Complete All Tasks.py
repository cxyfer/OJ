#
# @lc app=leetcode id=2589 lang=python3
# @lcpr version=30201
#
# [2589] Minimum Time to Complete All Tasks
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. Greedy + Sort
        2. Semgent Tree
        3. Stack + Binary Search
    """
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x : x[1]) # 按照結束時間排序
        vis = [False] * (tasks[-1][1] + 1) # vis[i] 表示第i個時間點是否在執行任務
        for st, ed, d in tasks:
            d -= sum(vis[st:ed+1]) # 減去可重疊執行任務的時間點
            if d <= 0:
                continue
            i = ed # 往前找未執行任務的時間點
            while d:
                if not vis[i]:
                    vis[i] = True
                    d -= 1
                i -= 1
        return sum(vis)
# @lc code=end



#
# @lcpr case=start
# [[2,3,1],[4,5,1],[1,5,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,2],[2,5,3],[5,6,2]]\n
# @lcpr case=end

#

