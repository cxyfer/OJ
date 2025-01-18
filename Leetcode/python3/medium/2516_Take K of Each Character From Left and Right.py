#
# @lc app=leetcode id=2516 lang=python3
# @lcpr version=30204
#
# [2516] Take K of Each Character From Left and Right
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """ 
        Sliding Window
        將問題轉換為在 s 中找到最長的子字串，使得子字串外至少有 k 個 a, b, c
        用 cnt 統計窗口外的字元數量，當 cnt[ch] < k 時，表示窗口外的字元數量不足，
        需要移動 left 指針來縮小窗口，直到 cnt[ch] >= k 為止。
    """
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        cnt = Counter(s) # 統計每種字元的數量
        if any(cnt[c] < k for c in "abc"): # 檢查是否每種字元都至少有 k 個
            return -1
        mx = left = 0
        for right, ch in enumerate(s):
            cnt[ch] -= 1
            while (cnt[ch] < k): # 窗口外的字元數量不足，需要移動 left 指針來縮小窗口
                cnt[s[left]] += 1
                left += 1
            mx = max(mx, right - left + 1) # 更新最大長度
        return n - mx # 返回需要移除的字元數量
# @lc code=end

sol = Solution()
print(sol.takeCharacters("aabaaaacaabc", 2)) # 8
print(sol.takeCharacters("a", 1)) # -1

#
# @lcpr case=start
# "aabaaaacaabc"\n2\n
# @lcpr case=end

# @lcpr case=start
# "a"\n1\n
# @lcpr case=end

#

