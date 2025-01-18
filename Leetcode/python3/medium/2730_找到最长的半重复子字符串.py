#
# @lc app=leetcode.cn id=2730 lang=python3
#
# [2730] 找到最长的半重复子字符串
#

# @lc code=start
class Solution:
    """
        Sliding window
    """
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        return self.solve1(s)
        # return self.solve2(s)
    def solve1(self, s: str) -> int:
        n = len(s)
        ans = 1
        left = 0 # 滑動窗口左端點
        same = 0 # 相鄰的相同字元數量
        for right in range(1, n):
            same += (s[right] == s[right - 1]) # 相鄰字元相同則 same += 1
            if same > 1: # 縮小窗口
                left += 1
                while s[left] != s[left - 1]: # 
                    left += 1
                same = 1
            ans = max(ans, right - left + 1) # 更新答案
        return ans
    def solve2(self, s: str) -> int:
        n = len(s)
        ans = 1
        left = 0 # 滑動窗口左端點
        last = -1 # 上一次重複字元的位置
        for right in range(1, n):
            if s[right] == s[right - 1]: # 相鄰字元相同
                if last != -1:
                    left = last + 1
                last = right - 1
            ans = max(ans, right - left + 1) # 更新答案
        return ans
# @lc code=end

