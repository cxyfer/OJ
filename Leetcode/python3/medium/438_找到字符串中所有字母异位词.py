#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
from preImport import *
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        cnt = Counter(s[:n-1])
        cnt_p = Counter(p)
        ans = []
        left, right = 0, n-1
        for right in range(n-1, m):
            cnt[s[right]] += 1
            if cnt == cnt_p:
                ans.append(left)
            cnt[s[left]] -= 1
            if cnt[s[left]] == 0:
                del cnt[s[left]]
            left += 1
        return ans
# @lc code=end
sol = Solution()
print(sol.findAnagrams("cbaebabacd","abc")) # [0,6]
print(sol.findAnagrams("abab","ab")) # [0,1,2]
print(sol.findAnagrams("baa","aa")) # [1]

