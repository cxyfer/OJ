# @algorithm @lc id=3199 lang=python3 
# @title distribute-candies-among-children-i


from en.Python3.mod.preImport import *
# @test(5,2)=3
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return self.solve2(n, limit)
    """
        1. Brute Force
    """
    def solve1(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(limit+1):
            for j in range(limit+1):
                k = n - i - j
                if k >= 0 and k <= limit:
                    ans += 1
        return ans
    """
        2. 排容原理
        a. 所有方案數：
            H(3, n) = C(n+2, n) = C(n+2, 2)
        b. 至少一人拿到超過 limit 個糖果的方案數：
            (先分(limit+1)給他，剩下的分給所有人)
            3 * H(3, n-(limit+1)) = 3 * C(n−(limit+1)+2, 2)
        c. 至少兩人拿到超過 limit 個糖果的方案數：
            3 * C(n−2⋅(limit+1)+2, 2)
    """

    def solve2(self, n: int, limit: int) -> int:
        if n > 3 * limit: # 三人都拿到超過 limit 個糖果，沒有方案
            return 0
        ans = comb(n + 2, 2)
        if n >= (limit + 1): # 至少一人拿到超過 limit 個糖果
            ans -= 3 * comb(n - limit + 1, 2)
        if n >= 2 * (limit + 1): # 至少兩人拿到超過 limit 個糖果
            ans += 3 * comb(n - 2 * limit, 2)
        return ans