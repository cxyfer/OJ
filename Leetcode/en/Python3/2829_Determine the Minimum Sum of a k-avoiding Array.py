# @algorithm @lc id=2811 lang=python3 
# @title determine-the-minimum-sum-of-a-k-avoiding-array


from en.Python3.mod.preImport import *
# @test(5,4)=18
# @test(2,6)=3
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # O(n)
        # hashmap = {}
        # ans = 0
        # count = 0
        # idx = 1
        # while count < n:
        #     if k-idx not in hashmap:
        #         count += 1
        #         ans += idx
        #     hashmap[idx] = idx
        #     idx += 1
        # return ans
        
        # O(1)
        m = min (k//2, n)
        # 1 + ... + m (m個)
        # k + ... + k+n-m-1 (n-m個)
        return (1+m)*m//2 + (2*k + n-m-1)*(n-m)//2