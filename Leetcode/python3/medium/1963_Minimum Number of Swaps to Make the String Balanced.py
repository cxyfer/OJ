#
# @lc app=leetcode id=1963 lang=python3
# @lcpr version=30204
#
# [1963] Minimum Number of Swaps to Make the String Balanced
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
    https://gdst.dev/posts/LC-1963/
"""
# @lc code=start
class Solution1:
    def minSwaps(self, s: str) -> int:
        st = []  # 維護未配對的 '[' 
        for ch in s:
            if ch == '[':
                st.append(ch)
            elif st:
                st.pop()
        return (len(st) + 1) // 2

class Solution2:
    def minSwaps(self, s: str) -> int:
        cnt = 0  # 未配對的 '[' 數量
        for ch in s:
            if ch == '[':
                cnt += 1
            elif cnt:
                cnt -= 1
        return (cnt + 1) // 2

class Solution(Solution1):
# class Solution(Solution2):
    pass     
# @lc code=end

sol = Solution()
print(sol.minSwaps("][]][]][][[["))

#
# @lcpr case=start
# "][]["\n
# @lcpr case=end

# @lcpr case=start
# "]]][[["\n
# @lcpr case=end

# @lcpr case=start
# "[]"\n
# @lcpr case=end

#

