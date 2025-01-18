#
# @lc app=leetcode id=1545 lang=python3
# @lcpr version=30204
#
# [1545] Find Kth Bit in Nth Binary String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ln = [0] # ln[i] = length of S_i
        for _ in range(n):
            ln.append(ln[-1] * 2 + 1)
        def find(n, k):
            if n == 1:
                return "0"
            mid = ln[n-1] + 1
            if k < mid:
                return find(n - 1, k)
            elif k == mid:
                return "1"
            else:
                return "1" if find(n-1, mid - (k - mid)) == "0" else "0"
        return find(n, k)
# @lc code=end

sol = Solution()
print(sol.findKthBit(3, 1)) # 0
print(sol.findKthBit(4, 11)) # 1

print(sol.findKthBit(3, 1)) # 0
print(sol.findKthBit(3, 2)) # 1
print(sol.findKthBit(3, 3)) # 1
print(sol.findKthBit(3, 4)) # 1
print(sol.findKthBit(3, 5)) # 0
print(sol.findKthBit(3, 6)) # 0
print(sol.findKthBit(3, 7)) # 1
#
# @lcpr case=start
# 3\n1\n
# @lcpr case=end

# @lcpr case=start
# 4\n11\n
# @lcpr case=end

#

