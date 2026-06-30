#
# @lc app=leetcode id=1358 lang=python3
# @lcpr version=30204
#
# [1358] Number of Substrings Containing All Three Characters
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. 越長越合法型滑動窗口
2. 維護每個字母最後出現的位置
   此時左端點可能是 [0, 1, 2, ..., min(last)]，貢獻 min(last) + 1 個子串
"""
# @lc code=start
class Solution1:
    def numberOfSubstrings(self, s: str) -> int:
        need = 3
        ans = left = 0
        cnt = [0] * 3
        for right, ch in enumerate(s):
            c = ord(ch) - ord("a")
            # 1. 入窗口
            cnt[c] += 1
            if cnt[c] == 1:
                need -= 1
            # 2. 出窗口，維持窗口在向左延伸即可滿足條件的狀態
            while need == 0:
                c = ord(s[left]) - ord("a")
                cnt[c] -= 1
                if cnt[c] == 0:
                    need += 1
                left += 1
            # 3. 累加答案，此時 [0, left - 1] 都是合法的左端點
            ans += left
        return ans


class Solution2:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        last = [-1] * 3
        for i, ch in enumerate(s):
            last[ord(ch) - ord("a")] = i
            # 此時 [0, min(last)] 都是合法的左端點
            ans += min(last) + 1
        return ans


# Solution = Solution1
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.numberOfSubstrings("abcabc")) # 10
print(sol.numberOfSubstrings("aaacb")) # 3
print(sol.numberOfSubstrings("abc")) # 1


#
# @lcpr case=start
# "abcabc"\n
# @lcpr case=end

# @lcpr case=start
# "aaacb"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n
# @lcpr case=end

#

