#
# @lc app=leetcode id=884 lang=python3
# @lcpr version=30204
#
# [884] Uncommon Words from Two Sentences
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # cnt = Counter(s1.split() + s2.split())
        # return [w for w, v in cnt.items() if v == 1]
        words1, words2 = s1.split(), s2.split()
        cnt1, cnt2 = Counter(words1), Counter(words2)
        ans = []
        for word in words1:
            if cnt1[word] == 1 and word not in words2:
                ans.append(word)
        for word in words2:
            if cnt2[word] == 1 and word not in words1:
                ans.append(word)
        return ans
# @lc code=end



#
# @lcpr case=start
# "this apple is sweet"\n"this apple is sour"\n
# @lcpr case=end

# @lcpr case=start
# "apple apple"\n"banana"\n
# @lcpr case=end

#

