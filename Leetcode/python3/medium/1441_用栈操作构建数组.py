#
# @lc app=leetcode.cn id=1441 lang=python3
#
# [1441] 用栈操作构建数组
#
from preImport import *
# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        m = len(target)
        ans = []
        i, j = 1, 0 # i is the current number, j is the index of target
        while i <= n and j < m:
            if target[j] == i: # 要這個數字
                ans.append("Push")
                j += 1
            else: # 不要這個數字
                ans.append("Push")
                ans.append("Pop")
            i += 1
        return ans
# @lc code=end

# @test([1,3],3)=["Push","Push","Pop","Push"]
# @test([1,2,3],3)=["Push","Push","Push"]
# @test([1,2],4)=["Push","Push"]
sol = Solution()