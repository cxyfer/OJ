#
# @lc app=leetcode.cn id=313 lang=python3
#
# [313] 超级丑数
#

import heapq
from typing import List

# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # Similar to 23. Merge k Sorted Lists
        if n == 1:
            return 1
        # Maintain a heap
        pq = []
        for prime in primes:
            heapq.heappush(pq, prime)
        idx = 0
        ans = 1
        
        while (idx < n-1):
            cur = heapq.heappop(pq)
            for prime in primes:
                heapq.heappush(pq, cur*prime)
            if cur != ans:
                ans = cur
                idx += 1
        return ans
        
# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    print(sol.nthSuperUglyNumber(12, [2,7,13,19]))
    print(sol.nthSuperUglyNumber(1, [2,3,5]))
    # 1092889481
    print(sol.nthSuperUglyNumber(100000, [2,3,5,7,11,13,17,19,23,29,31,41,43,47,53,59,61,71,73,79,83,89,97,101,103,107,109,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251]))
