#
# @lc app=leetcode id=2734 lang=python3
# @lcpr version=30204
#
# [2734] Lexicographically Smallest String After Substring Operation
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def smallestString(self, s: str) -> str:
        lst = list(s)
        flag = False
        for i, ch in enumerate(lst):
            if flag and ch == 'a': # 改過，且改 a 會讓字典序變大
                break
            if ch != 'a':
                flag = True
                lst[i] = chr(ord(ch) - 1)
        if not flag: # 全部都是 a
            lst[-1] = 'z'
        return ''.join(lst)
# @lc code=end



#
# @lcpr case=start
# "cbabc"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n
# @lcpr case=end

# @lcpr case=start
# "acbbc"\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n
# @lcpr case=end

#

