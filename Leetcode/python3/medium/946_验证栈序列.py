#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#
from preImport import *
# @lc code=start
class Solution:
    """
        Stack
    """
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        st = []
        for x in pushed:
            st.append(x)
            while st and st[-1] == popped[i]:
                st.pop()
                i += 1
        return not st
# @lc code=end

