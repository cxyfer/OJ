#
# @lc app=leetcode id=2537 lang=python3
#
# [2537] Count the Number of Good Subarrays
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1 -> 0
2 -> comb(2, 2) = 1
3 -> comb(3, 2) = 3
4 -> comb(4, 2) = 6
"""
# @lc code=start
MAX_N = int(1e5)
comb = [[0] * 3 for _ in range(MAX_N + 1)]
for i in range(MAX_N + 1):
    comb[i][0] = 1

for x in range(1, MAX_N + 1):
    for y in range(1, min(x + 1, 3)):
        comb[x][y] = comb[x - 1][y] + comb[x - 1][y - 1]

for x in range(1, MAX_N + 1):
    for y in range(1, 3):
        assert comb[x][y] == math.comb(x, y), f"{x}, {y}, {comb[x][y]}, {math.comb(x, y)}"

class Solution1:
    def countGood(self, nums: List[int], k: int) -> int:
        ans = cur = left = 0
        cnt = defaultdict(int)
        for right, x in enumerate(nums):
            cur -= comb[cnt[x]][2]   
            cnt[x] += 1
            cur += comb[cnt[x]][2]
            while cur >= k:
                y = nums[left]
                cur -= comb[cnt[y]][2]
                cnt[y] -= 1
                cur += comb[cnt[y]][2]
                left += 1
            ans += left
        return ans
    
class Solution2:
    def countGood(self, nums: List[int], k: int) -> int:
        ans = cur = left = 0
        cnt = defaultdict(int)
        for right, x in enumerate(nums):
            cur += cnt[x]
            cnt[x] += 1
            while cur >= k:
                y = nums[left]
                cnt[y] -= 1
                cur -= cnt[y]
                left += 1
            ans += left
        return ans
    
# Solution = Solution1 
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.countGood([1,1,1,1,1], 10))  # 1
print(sol.countGood([3,1,4,3,2,2,4], 2))  # 4
print(sol.countGood([2,1,3,1,2,2,3,3,2,2,1,1,1,3,1], 11))  # 21


