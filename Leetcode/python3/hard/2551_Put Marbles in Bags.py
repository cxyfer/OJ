#
# @lc app=leetcode id=2551 lang=python3
#
# [2551] Put Marbles in Bags
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Greedy + Sorting: O(nlogn)
2. Greedy + Heap: O(nlogk)

核心思路都是貪心，利用以下性質：
1. 若選擇 [i, j] 區間，則 j + 1 必選，故可以將 weights[i] + weights[i+1] 視為一個 pair
2. 頭尾 weights[0] 和 weights[n-1] 必選，故在中間的 n - 1 個 pair 中選擇 k - 1 個即可
"""
# @lc code=start
class Solution1:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        pairs = [x + y for x, y in pairwise(weights)]
        pairs.sort()
        return sum(pairs[-(k-1):]) - sum(pairs[:(k-1)])
    
class Solution2:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        hp1, hp2 = [], []  # 維護大小為 k-1 的 Min/Max Heap 保存前 k-1 個最大/最小 pair
        for x, y in pairwise(weights):
            pair = x + y
            if len(hp1) < k - 1:
                heappush(hp1, pair)
            else:
                heappushpop(hp1, pair)
            if len(hp2) < k - 1:
                heappush(hp2, -pair)
            else:
                heappushpop(hp2, -pair)
        return sum(hp1) + sum(hp2)

Solution = Solution1
# Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.putMarbles([25,74,16,51,12,48,15,5], 1))  # 0
print(sol.putMarbles([1,4,2,5,2], 3))  # 3