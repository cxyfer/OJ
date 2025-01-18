# @algorithm @lc id=985 lang=python3 
# @title bag-of-tokens


from en.Python3.mod.preImport import *
# @test([100],50)=0
# @test([200,100],150)=1
# @test([100,200,300,400],200)=2
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