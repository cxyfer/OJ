#
# @lc app=leetcode id=1002 lang=python3
# @lcpr version=30203
#
# [1002] Find Common Characters
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])
        for word in words:
            cnt &= Counter(word)
        return [ch for ch, v in cnt.items() for _ in range(v)]
# @lc code=end



#
# @lcpr case=start
# ["bella","label","roller"]\n
# @lcpr case=end

# @lcpr case=start
# ["cool","lock","cook"]\n
# @lcpr case=end

#

