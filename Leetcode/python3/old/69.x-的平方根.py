#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while (left <= right): # [left, right]
            middle = left + (right-left)//2
            if middle*middle == x:
                return middle
            elif middle*middle < x:
                left = middle + 1
            else:
                right = middle - 1
        return right
# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    print(sol.mySqrt(4))
    print(sol.mySqrt(8))
    print(sol.mySqrt(177))
