#
# @lc app=leetcode id=2054 lang=python3
# @lcpr version=30204
#
# [2054] Two Best Non-Overlapping Events
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key=lambda x: x[0]) # 按開始時間排序
        hp = [] # Min Heap (end, value)
        ans = mx = 0
        for i in range(n):
            while hp and hp[0][0] < events[i][0]: # 結束時間小於當前事件的開始時間
                mx = max(mx, heappop(hp)[1]) # 更新最大值
            ans = max(ans, mx + events[i][2]) # 更新答案
            heappush(hp, (events[i][1], events[i][2])) # 加入當前事件
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,3,2],[4,5,2],[2,4,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,2],[4,5,2],[1,5,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,5,3],[1,5,1],[6,6,5]]\n
# @lcpr case=end

#

