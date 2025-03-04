#
# @lc app=leetcode.cn id=1328 lang=python3
# @lcpr version=30204
#
# [1328] 破坏回文串
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        lst = list(palindrome)
        # 找到第一個不為 'a' 的字元，並將其變為 'a'，注意不能改中心字元
        # 且由於原本的palindrome是回文，所以只需要檢查一半即可
        for i in range(n // 2):
            if lst[i] != 'a':
                lst[i] = 'a'
                break
        else:  # 如果沒有找到，則代表所有非中心字元都是 'a'，則將最後一個字元變為 'b'
            lst[-1] = 'b'
        return ''.join(lst)
# @lc code=end



#
# @lcpr case=start
# "abccba"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#

