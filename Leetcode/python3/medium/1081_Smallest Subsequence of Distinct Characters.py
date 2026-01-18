#
# @lc app=leetcode id=1081 lang=python3
# @lcpr version=30201
#
# [1081] Smallest Subsequence of Distinct Characters
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Greedy + Stack
Similar to 402. Remove K Digits
Very similar to 3816. Lexicographically Smallest String After Deleting Duplicate Characters
Same as 316. Remove Duplicate Letters
"""
# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        left = Counter(s)
        selected = set()
        st = []
        for ch in s:
            if ch not in selected:
                while st and st[-1] > ch and left[st[-1]] > 0:
                    selected.remove(st.pop())
                st.append(ch)
                selected.add(ch)
            left[ch] -= 1
        return ''.join(st)
# @lc code=end



#
# @lcpr case=start
# "bcabc"\n
# @lcpr case=end

# @lcpr case=start
# "cbacdcbc"\n
# @lcpr case=end

#

