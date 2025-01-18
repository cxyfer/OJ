#
# @lc app=leetcode.cn id=2904 lang=python3
#
# [2904] 最短且字典序最小的美丽子字符串
#

# @lc code=start
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = s
        n = len(s)
        pos = [i for i in range(n) if s[i] == '1']
        if len(pos) < k:
            return ""
        for i in range(len(pos)-k+1):
            cur = s[pos[i]:pos[i+k-1]+1]
            if len(cur) < len(ans):
                ans = cur
            elif len(cur) == len(ans):
                ans = min(ans, cur)
        return ans

# @lc code=end
sol = Solution()
print(sol.shortestBeautifulSubstring("100011001",3)) #="11001"
print(sol.shortestBeautifulSubstring("1011",2)) #="11"
print(sol.shortestBeautifulSubstring("000",1)) #=""

