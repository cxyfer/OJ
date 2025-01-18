#
# @lc app=leetcode id=2614 lang=python3
# @lcpr version=30202
#
# [2614] Prime In Diagonal
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(n):
            if n < 2 or n % 2 == 0 and n != 2: # 先判斷是否為2的倍數
                return False
            for i in range(3, int(n ** 0.5) + 1, 2): # 之後只判斷是否為奇數的倍數
                if n % i == 0:
                    return False
            return True
        n = len(nums)
        ans = 0
        for i, row in enumerate(nums):
            for x in [row[i], row[n-1-i]]:
                if x > ans and is_prime(x):
                    ans = x
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[5,6,7],[9,10,11]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[5,17,7],[9,11,10]]\n
# @lcpr case=end

#

