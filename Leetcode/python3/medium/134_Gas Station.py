#
# @lc app=leetcode id=134 lang=python3
# @lcpr version=30204
#
# [134] Gas Station
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        left = tot = 0
        for right in range(2 * n):
            tot += gas[right % n] - cost[right % n]
            while tot < 0 and left <= right:
                tot -= gas[left % n] - cost[left % n]
                left += 1
            if right - left + 1 == n:
                return left % n
        return -1
    
class Solution2:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        ans = cur = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            cur += g - c
            if cur < 0:
                cur = 0
                ans = i + 1
        return ans

# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])) # 3
print(sol.canCompleteCircuit([2,3,4], [3,4,3])) # -1

#
# @lcpr case=start
# [1,2,3,4,5]\n[3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n[3,4,3]\n
# @lcpr case=end

#

