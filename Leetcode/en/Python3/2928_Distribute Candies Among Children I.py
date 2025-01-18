# @algorithm @lc id=3199 lang=python3 
# @title distribute-candies-among-children-i


from en.Python3.mod.preImport import *
# @test(5,2)=3
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(limit+1):
            for j in range(limit+1):
                k = n - i - j
                if k >= 0 and k <= limit:
                    ans += 1
        return ans