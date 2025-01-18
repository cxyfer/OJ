#
# @lc app=leetcode id=826 lang=python3
# @lcpr version=30202
#
# [826] Most Profit Assigning Work
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. Sort + Two Pointers
            O(nlogn + mlogm)
        2. Sort + Binary Search
            O(nlogn + mlogn)
    """
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        return self.solve1(difficulty, profit, worker)
        # return self.solve2(difficulty, profit, worker)
    def solve1(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n, m = len(difficulty), len(worker)
        tasks = sorted(zip(difficulty, profit))
        worker.sort()
        ans, i, mx = 0, 0, 0
        # for j, w in enumerate(worker):
        for w in worker:
            while i < n and tasks[i][0] <= w: # find the last task that can be done
                mx = max(mx, tasks[i][1]) # max profit
                i += 1
            ans += mx
        return ans
    def solve2(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n, m = len(difficulty), len(worker)
        tasks = sorted(zip(difficulty, profit)) # sort by difficulty
        max_profit = [0] * (n) # max_profit[i] = max profit of tasks[0:i+1]
        max_profit[0] = tasks[0][1]
        for i in range(1, n):
            max_profit[i] = max(max_profit[i-1], tasks[i][1])
        ans = 0
        for ability in worker:
            idx = bisect_right(tasks, (ability, float("inf"))) - 1 # find the last task that can be done
            ans += max_profit[idx] if idx >= 0 else 0
        return ans
# @lc code=end

sol = Solution()
print(sol.maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7])) # 100
print(sol.maxProfitAssignment([85,47,57], [24,66,99], [40,25,25])) # 0

#
# @lcpr case=start
# [2,4,6,8,10]\n[10,20,30,40,50]\n[4,5,6,7]\n
# @lcpr case=end

# @lcpr case=start
# [85,47,57]\n[24,66,99]\n[40,25,25]\n
# @lcpr case=end

#

