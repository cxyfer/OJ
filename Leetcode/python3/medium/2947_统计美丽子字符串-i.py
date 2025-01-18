#
# @lc app=leetcode.cn id=2947 lang=python3
#
# [2947] 统计美丽子字符串 I
#

# @lc code=start
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        vowels = consonants = 0
        pre_v = [0] * (n+1)  
        pre_c = [0] * (n+1)
        for i in range(n):
            if s[i] in "aeiou":
                vowels += 1
            else:
                consonants += 1
            pre_v[i+1] = vowels
            pre_c[i+1] = consonants
        for i in range(n): # 枚舉起點
            for j in range(i + 1, n+1): # 枚舉終點
                vowels = pre_v[j] - pre_v[i]
                consonants = pre_c[j] - pre_c[i]
                if vowels == consonants and vowels * consonants % k == 0:
                    ans += 1
        return ans
# @lc code=end

