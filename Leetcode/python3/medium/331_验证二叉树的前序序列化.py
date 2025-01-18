#
# @lc app=leetcode.cn id=331 lang=python3
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        cnt = 1 # number of available slots
        for ch in preorder.split(','):
            if cnt == 0:
                return False
            if ch == '#': # null node, consume a slot
                cnt -= 1
            else: # non-null node, consume a slot and create two more slots
                cnt += 1
        return cnt == 0
# @lc code=end
sol = Solution()
print(sol.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")) # True
print(sol.isValidSerialization("1,#")) # False
print(sol.isValidSerialization("9,#,#,1")) # False