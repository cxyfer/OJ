#
# @lc app=leetcode id=1455 lang=python3
# @lcpr version=30204
#
# [1455] Check If a Word Occurs As a Prefix of Any Word in a Sentence
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for idx, word in enumerate(words):
            if word.startswith(searchWord):
                return idx + 1
        return -1
# @lc code=end



#
# @lcpr case=start
# "i love eating burger"\n"burg"\n
# @lcpr case=end

# @lcpr case=start
# "this problem is an easy problem"\n"pro"\n
# @lcpr case=end

# @lcpr case=start
# "i am tired"\n"you"\n
# @lcpr case=end

#

