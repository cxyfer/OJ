#
# @lc app=leetcode id=2490 lang=python3
# @lcpr version=30204
#
# [2490] Circular Sentence
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)
        for i in range(n):
            if words[i][-1] != words[(i + 1) % n][0]:
                return False
        return True
        
class Solution2:
    def isCircularSentence(self, sentence: str) -> bool:
        for i, ch in enumerate(sentence):
            if ch == " " and sentence[i - 1] != sentence[i + 1]:
                return False
        return sentence[0] == sentence[-1]

class Solution(Solution1):
# class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# "leetcode exercises sound delightful"\n
# @lcpr case=end

# @lcpr case=start
# "eetcode"\n
# @lcpr case=end

# @lcpr case=start
# "Leetcode is cool"\n
# @lcpr case=end

#

