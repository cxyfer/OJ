#
# @lc app=leetcode id=1081 lang=python3
# @lcpr version=30201
#
# [1081] Smallest Subsequence of Distinct Characters
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Greedy + Stack
        Similar to 402. Remove K Digits
        Same as 316. Remove Duplicate Letters
    """
    def smallestSubsequence(self, s: str) -> str:
        cnt = Counter(s)
        st = []
        selected = set()
        for ch in s:
            if ch not in selected: # 這個字母還沒被選過
                # 這個字母比前面的字母小，且前面的字母還有剩餘，就把前面的字母刪掉(反悔)
                while st and st[-1] > ch and cnt[st[-1]] > 0:
                    selected.remove(st.pop())
                st.append(ch) # 把這個字母加入答案
                selected.add(ch) # 標記為已選擇
            cnt[ch] -= 1
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

