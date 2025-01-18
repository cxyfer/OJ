#
# @lc app=leetcode id=2398 lang=python3
# @lcpr version=30204
#
# [2398] Maximum Number of Robots Within Budget
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Monotonic Queue
    """
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        ans = 0
        q = deque() # 維護一個「單調遞減」的佇列，存的是 chargeTimes 的 index，chargeTimes[q[0]] 即為當前 max(chargeTimes)
        s = 0 # 維護 sum(runningCosts)
        left = 0 # 維護一個 sliding window 的左端點
        for right, (t, c) in enumerate(zip(chargeTimes, runningCosts)):
            # 1. 入窗口
            while q and t >= chargeTimes[q[-1]]:
                q.pop()
            q.append(right) 
            s += c
            
            # 2. 出窗口
            # cost = max(chargeTimes) + k * sum(runningCosts)
            while q and chargeTimes[q[0]] + (right - left + 1) * s > budget:
                if q[0] == left: # 最大值在左端點，需要從 queue 中移除
                    q.popleft()
                s -= runningCosts[left]
                left += 1
            
            # 3. 更新答案
            ans = max(ans, right - left + 1)
        return ans
# @lc code=end

#
# @lcpr case=start
# [3,6,1,3,4]\n[2,1,3,4,5]\n25\n
# @lcpr case=end

# @lcpr case=start
# [11,12,19]\n[10,8,7]\n19\n
# @lcpr case=end

#

