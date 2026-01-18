#
# @lc app=leetcode id=3816 lang=python3
#
# [3816] Lexicographically Smallest String After Deleting Duplicate Characters
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Monotonic Stack + Greedy
Similar to 316. Remove Duplicate Letters
考慮哪些元素應該被刪除？
若元素 b 被刪除後可以被字典序更小的 a 替代，則 b 應該被刪除
但刪除時需要前面或後面未被刪除的元素中還存在相同的元素
賽時用了兩個 Counter 對前後分別計數，但其實只需要一個即可
最後檢查後綴中是否還有可以被刪除的元素
"""
# @lc code=start
class Solution1a:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        cnt = defaultdict(int)
        suf = Counter(s)
        st = []
        for ch in s:
            suf[ch] -= 1
            while st and st[-1] > ch and (cnt[st[-1]] > 1 or suf[st[-1]] > 0):
                cnt[st.pop()] -= 1
            st.append(ch)
            cnt[ch] += 1
        while st and cnt[st[-1]] > 1:
            cnt[st.pop()] -= 1
        return ''.join(st)

class Solution1b:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        left = Counter(s)
        st = []
        for ch in s:
            # st[-1] 的位置可以被 ch 替代，使得字典序更小
            while st and st[-1] > ch and left[st[-1]] > 1:
                left[st.pop()] -= 1
            st.append(ch)
        # 還需要檢查後綴中是否還有可以被刪除的元素，使得字典序更小
        while st and left[st[-1]] > 1:
            left[st.pop()] -= 1
        return ''.join(st)

Solution = Solution1b
# @lc code=end

sol = Solution()
print(sol.lexSmallestAfterDeletion("aaccb"))  # "aacb"
print(sol.lexSmallestAfterDeletion("abcab"))  # "abc"
print(sol.lexSmallestAfterDeletion("bbcac"))  # "bac"
print(sol.lexSmallestAfterDeletion("bcacb"))  # "acb"