# @algorithm @lc id=3375 lang=python3 
# @title kth-smallest-amount-with-single-denomination-combination


from en.Python3.mod.preImport import *
# @test([3,6,9],3)=9
# @test([5,2],7)=12
class Solution:
    """
        二分搜尋 + 排容原理 + 集合枚舉
        Similar to 1201. Ugly Number III

        枚舉一個數字 m ，可以利用排容原理計算 m 是第幾小的數字(即有多少組合小於 m)。
        由於 coins 長度小於 15 ，可以利用bitmask來枚舉所有的組合。
        由於 m 越大就代表比 m 小的數字越多，因此具備單調性，可以使用二分搜尋。
    """
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        def check(m: int) -> bool: # 計算比 m 小的組合數量有幾個，返回 m 是否在第 k 小的組合以後
            cnt = 0
            for i in range(1, 1 << n):
                cur = 1 # lcm
                for j, coin in enumerate(coins):
                    if i >> j & 1:
                        cur = math.lcm(cur, coin)
                cnt += m // cur if bin(i).count('1') & 1 else -(m // cur)
            return cnt >= k
        # return bisect_left(range(min(coins) * k), True, k, key=check)
        left, right = k - 1, min(coins) * k # [left, right]
        while left <= right: 
            mid = (left + right) // 2 
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left