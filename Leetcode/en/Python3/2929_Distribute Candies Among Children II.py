# @algorithm @lc id=3201 lang=python3 
# @title distribute-candies-among-children-ii


from en.Python3.mod.preImport import *
# @test(5,2)=3
# @test(3,3)=10
class Solution:
    """
        排容原理
    """
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > 3 * limit:
            return 0
        ans = comb(n + 2, 2)
        if n > limit:
            ans -= 3 * comb(n - limit + 1, 2)
        if n - 2 >= 2 * limit:
            ans += 3 * comb(n - 2 * limit, 2)
        return ans