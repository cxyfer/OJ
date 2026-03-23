#
# @lc app=leetcode id=3877 lang=python3
#
# [3877] Minimum Removals to Achieve Target XOR
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def minRemovals(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mid = (n + 1) // 2

        def build(arr: list[int]) -> defaultdict:
            m = len(arr)
            mp = defaultdict(lambda: float("-inf"))
            for msk in range(1 << m):
                v = 0
                for i, x in enumerate(arr):
                    if (msk >> i) & 1:
                        v ^= x
                mp[v] = max(mp[v], msk.bit_count())
            return mp

        mp1 = build(nums[:mid])
        mp2 = build(nums[mid:])
        ans = float("inf")
        for k, v in mp1.items():
            ans = min(ans, n - (v + mp2[k ^ target]))
        return ans if ans != float("inf") else -1

class Solution2:
    def minRemovals(self, nums: List[int], target: int) -> int:
        n = len(nums)

        f = defaultdict(lambda: float("-inf"))
        f[0] = 0
        for x in nums:
            nf = f.copy()
            for k, v in f.items():
                nf[k ^ x] = max(nf[k ^ x], v + 1)
            f = nf
        return n - f[target] if f[target] != float("-inf") else -1

# Solution = Solution1
Solution = Solution2
# @lc code=end

