#
# @lc app=leetcode id=3042 lang=python3
# @lcpr version=30204
#
# [3042] Count Prefix and Suffix Pairs I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i, w1 in enumerate(words):
            for j in range(i+1, len(words)):
                w2 = words[j]
                if w2.startswith(w1) and w2.endswith(w1):
                    ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# ["a","aba","ababa","aa"]\n
# @lcpr case=end

# @lcpr case=start
# ["pa","papa","ma","mama"]\n
# @lcpr case=end

# @lcpr case=start
# ["abab","ab"]\n
# @lcpr case=end

#

