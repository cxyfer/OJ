#
# @lc app=leetcode.cn id=1652 lang=python3
#
# [1652] 拆炸弹
#
from preImport import *
# @lc code=start
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        ans = [-1] * n
        for i in range(n):
            s = 0
            if k > 0:
                for j in range(1, k+1):
                    s += code[(i+j)%n]
            else:
                for j in range(1, -k+1):
                    s += code[(i-j)%n]
            ans[i] = s
        return ans
# @lc code=end
sol = Solution()
print(sol.decrypt([5,7,1,4],3)) # [12,10,16,13]
print(sol.decrypt([1,2,3,4],0)) # [0,0,0,0]
print(sol.decrypt([2,4,9,3],-2)) # [12,5,6,13]