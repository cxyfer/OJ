#
# @lc app=leetcode id=3163 lang=python3
# @lcpr version=30202
#
# [3163] String Compression III
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        ans = ""
        i = 0
        while i < n: # 分組循環
            st = i
            while i < n and i - st < 9 and word[i] == word[st]:
                i += 1
            ans += str(i - st) + word[st]
        return ans
# @lc code=end



#
# @lcpr case=start
# "abcde"\n
# @lcpr case=end

# @lcpr case=start
# "aaaaaaaaaaaaaabb"\n
# @lcpr case=end

#

