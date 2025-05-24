#
# @lc app=leetcode id=2942 lang=python3
#
# [2942] Find Words Containing Character
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
# @lc code=end

