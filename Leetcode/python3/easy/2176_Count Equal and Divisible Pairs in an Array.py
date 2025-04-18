#
# @lc app=leetcode id=2176 lang=python3
#
# [2176] Count Equal and Divisible Pairs in an Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                ans += nums[i] == nums[j] and (i * j) % k == 0
        return ans

MX = 105
divisors = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i, MX, i):
        divisors[j].append(i)

class Solution2:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        divs = divisors[k]
        cnt = defaultdict(lambda: defaultdict(int))
        for j, x in enumerate(nums):
            ans += cnt[x][k // math.gcd(j, k)]
            for d in divs:
                if j % d == 0:
                    cnt[x][d] += 1
        return ans

# Solution = Solution1
Solution = Solution2
# @lc code=end
