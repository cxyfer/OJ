#
# @lc app=leetcode.cn id=948 lang=python3
#
# [948] 令牌放置
#
from preImport import *
# @lc code=start
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        if n == 0:
            return 0
        tokens.sort()
        if power < tokens[0]:
            return 0
        left, right = 0, n - 1
        ans = score = 0
        while left <= right:
            if power < tokens[left]:
                if score > 0:
                    score -= 1
                    power += tokens[right]
                    right -= 1
                else:
                    break
            else:
                score += 1
                power -= tokens[left]
                left += 1
                ans = max(ans, score)
        return ans
# @lc code=end
sol = Solution()
print(sol.bagOfTokensScore([100],50)) # 0
print(sol.bagOfTokensScore([200,100],150)) # 1
print(sol.bagOfTokensScore([100,200,300,400],200)) # 2
