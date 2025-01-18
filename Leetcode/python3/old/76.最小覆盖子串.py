#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
from collections import Counter
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Sliding window, two pointers
        # Similar to 209. Minimum Size Subarray Sum
        # Similar to 904. Fruit Into Baskets
        ans = ""
        cnt = Counter()
        cnt_t = Counter(t)
        left = 0
        for right, char in enumerate(s):
            cnt[char] += 1
            while all(cnt[char] >= cnt_t[char] for char in cnt_t): # 符合條件，開始縮小窗口
                cnt[s[left]] -= 1
                if not ans or len(ans) > (right - left + 1): # 更新答案
                    ans = s[left:right+1]
                left += 1
        return ans

# @lc code=end

