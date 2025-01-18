#
# @lc app=leetcode id=3378 lang=python3
# @lcpr version=30204
#
# [3378] Count Connected Components in LCM Graph
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
lcm(a, b) = a * b / gcd(a, b) <= threshold
-> a * b <= threshold * gcd(a, b)
"""

class UnionFind:
    def __init__(self, n):
        self.pa = list(range(n))
        self.sz = [1] * n
        self.cnt = n

    def find(self, x):
        while self.pa[x] != x:
            self.pa[x] = self.pa[self.pa[x]]
            x = self.pa[x]
        return x

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.sz[px] < self.sz[py]:
            px, py = py, px
        self.pa[py] = px
        self.sz[px] += self.sz[py]
        self.cnt -= 1
        return True

# 預處理因數
N = (int(2e5) + 5)
factors = [[] for _ in range(N)]
for i in range(1, N):
    for j in range(i, N, i):
        factors[j].append(i)

class Solution:
    def countComponents(self, nums, threshold):
        n = len(nums)
        nums.sort()
        facs = defaultdict(list) # 因數 -> 數字索引
        for i, x in enumerate(nums):
            if x > threshold:
                continue
            for f in factors[x]:
                if f > threshold:
                    break
                facs[f].append(i)

        uf = UnionFind(n)
        for g, ids in facs.items(): # 枚舉 gcd
            limit = threshold * g
            x = ids[0]
            for y in ids[1:]:
                if nums[x] * nums[y] <= limit:
                    uf.union(x, y)
        return uf.cnt
# @lc code=end

sol = Solution()
print(sol.countComponents([2,4,8,3,9], 5)) # 4
print(sol.countComponents([2,4,8,3,9,12], 10)) # 2
print(sol.countComponents([31,33,11], 90)) # 2
print(sol.countComponents([41,1,20], 80)) # 1
print(sol.countComponents([18,57,98,81], 170)) # 3
print(sol.countComponents([91,39,2,70], 194)) # 1
print(sol.countComponents([53,75,25,20], 183)) # 2
print(sol.countComponents([69,52,99,12,18,119], 240)) # 3

#
# @lcpr case=start
# [2,4,8,3,9]\n5\n
# @lcpr case=end

# @lcpr case=start
# [2,4,8,3,9,12]\n10\n
# @lcpr case=end

#

