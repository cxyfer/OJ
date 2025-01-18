#
# @lc app=leetcode id=520 lang=python3
# @lcpr version=30204
#
# [520] Detect Capital
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def detectCapitalUse(self, word: str) -> bool:
        # return word.isupper() or word.islower() or word.istitle()
        ck1 = ck2 = ck3 = True
        for i, ch in enumerate(word):
            if ch.islower():
                ck1 = False
                if i == 0:
                    ck3 = False
            else:
                ck2 = False
                if i > 0:
                    ck3 = False
        return ck1 or ck2 or ck3
    
class Solution2:
    def detectCapitalUse(self, word: str) -> bool:
        cnt = sum(ch.isupper() for ch in word)
        return cnt == 0 or cnt == len(word) or cnt == 1 and word[0].isupper()

class Solution(Solution1):
# class Solution(Solution2):
    pass
# @lc code=end

#
# @lcpr case=start
# "USA"\n
# @lcpr case=end

# @lcpr case=start
# "FlaG"\n
# @lcpr case=end

#

