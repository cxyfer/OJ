#
# @lc app=leetcode.cn id=2709 lang=python3
#
# [2709] 最大公约数遍历
#
from preImport import *
# @lc code=start

# Initialize the list of prime factors for each number
MAXN = 10 ** 5 + 5
fac = defaultdict(list)
for i in range(2, MAXN):
    if not fac[i]: # i is prime
        for j in range(i, MAXN, i): # mark all multiples of i
            fac[j].append(i)

class Solution:
    """
        Connect all pairs of numbers which have same prime factor.
        If all numbers are connected, return True.
        -> Union Find
    """
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        mx = max(nums)

        pa = list(range(n + mx + 1)) # parent

        def find(x): # find root
            if pa[x] != x:
                pa[x] = find(pa[x]) # path compression
            return pa[x]

        def union(x, y):
            pa[find(x)] = find(y)

        for i, num in enumerate(nums):
            for p in fac[num]:
                union(i, n + p) # connect node i to node n+p, all nodes connected to n+p have prime factor p

        # check if all numbers in range(n) are connected
        r = find(0)
        for i in range(1, n):
            if find(i) != r:
                return False
        return True
# @lc code=end
sol = Solution()
print(sol.canTraverseAllPairs([2,3,6])) # True
# print(sol.canTraverseAllPairs([3,9,5])) # False
# print(sol.canTraverseAllPairs([4,3,12,8])) # True
[960,210]
