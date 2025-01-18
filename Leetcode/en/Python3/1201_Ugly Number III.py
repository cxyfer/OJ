# @algorithm @lc id=1307 lang=python3 
# @title ugly-number-iii


from en.Python3.mod.preImport import *
# @test(3,2,3,5)=4
# @test(4,2,3,4)=6
# @test(5,2,11,13)=10
class Solution:
    """
        二分搜尋 + 排容原理 + 集合枚舉
        Similar to 3116. Kth Smallest Amount With Single Denomination Combination
    """
    def nthUglyNumber(self, k: int, a: int, b: int, c: int) -> int:
        def check(m: int) -> bool: # 計算比 m 小的組合數量有幾個，返回 m 是否在第 n 小的組合以後
            cnt = 0
            for i in range(1, 1 << 3):
                cur = 1 # lcm
                for j, x in enumerate([a, b, c]):
                    if i >> j & 1:
                        cur = math.lcm(cur, x)
                cnt += m // cur if i.bit_count() & 1 else -(m // cur)
            return cnt >= k
        # return bisect_left(range(min([a, b, c]) * k), True, k, key=check)
        left, right = k - 1, min([a, b, c]) * k # [left, right]
        while left <= right: 
            mid = (left + right) // 2 
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left