#
# @lc app=leetcode id=1863 lang=python3
# @lcpr version=30202
#
# [1863] Sum of All Subset XOR Totals
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. Brute force + Backtracking / Bit Manipulation
          O(n * 2^n)
        2. Math + Bit Manipulation
          按位考慮，考慮每個子集中該位 1 的個數
          - 若該子集中該位 1 的個數為奇數，則該位的 XOR 值為 1
          - 若該子集中該位 1 的個數為偶數，則該位的 XOR 值為 0

          接著考慮所有子集中該位的 XOR 和
          - 若所有元素中的該位皆為 0 ，則所有 2^n 個子集中，該位的 XOR 和顯然為 0
          - 若至少有一個元素中的該位為 1，則總共有 2^(n-1) 個子集中該位 1 的個數為奇數、2^(n-1) 個子集中該位 1 的個數為偶數，證明參考官解

          若第 i 位中至少有一個元素的該位為 1，則該位對答案的貢獻為 2^(n-1) * 2^i
          所以只要用判斷所有元素中是否有一個元素的該位為 1 即可，可以計算所有元素的 OR 值，最後左移 n-1 位即可

          O(n)
    """
    def subsetXORSum(self, nums: List[int]) -> int:
        # return self.solve1(nums)
        return self.solve2(nums)
    def solve1(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1 << n): # 枚舉所有子集，狀態壓縮
            cur = 0 # 當前子集的 XOR 和
            for j in range(n):
                if i & (1 << j): # 當前元素是否在子集中
                    cur ^= nums[j]
            ans += cur
        return ans
    def solve2(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for x in nums:
            res |= x
        return res << (n - 1)
# @lc code=end



#
# @lcpr case=start
# [1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,6]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,6,7,8]\n
# @lcpr case=end

#

