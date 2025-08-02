#
# @lc app=leetcode id=2561 lang=python3
#
# [2561] Rearranging Fruits
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1a:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt1, cnt2 = Counter(basket1), Counter(basket2)
        mn = min(min(cnt1.keys()), min(cnt2.keys()))
        for k, v in (cnt1 + cnt2).items():
            if v & 1:
                return -1
            cnt1[k] -= (v >> 1)
            cnt2[k] -= (v >> 1)
            if cnt1[k] <= 0:
                del cnt1[k]
            if cnt2[k] <= 0:
                del cnt2[k]

        keys1, keys2 = sorted(cnt1.keys()), sorted(cnt2.keys(), reverse=True)
        i, j = 0, 0
        ans = 0
        while i < len(keys1) and j < len(keys2):
            k1, k2 = keys1[i], keys2[j]
            cost = min(k1, k2, mn * 2)
            ans += (v := min(cnt1[k1], cnt2[k2])) * cost
            cnt1[k1] -= v
            cnt2[k2] -= v
            i += (cnt1[k1] == 0)
            j += (cnt2[k2] == 0)
        return ans
    
class Solution1b:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt1, cnt2 = Counter(basket1), Counter(basket2)
        mn = min(min(cnt1.keys()), min(cnt2.keys()))
        A, B = [], []
        for k, v in (cnt1 + cnt2).items():
            if v & 1:
                return -1
            A.extend([k] * (cnt1[k] - (v >> 1)))
            B.extend([k] * (cnt2[k] - (v >> 1)))
        return sum(min(a, b, mn * 2) for a, b in zip(sorted(A), sorted(B, reverse=True)))
    
class Solution2:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = defaultdict(int)
        for x, y in zip(basket1, basket2):
            cnt[x] += 1
            cnt[y] -= 1
        mn = min(cnt.keys())
        A, B = [], []
        for k, v in cnt.items():
            if v & 1:
                return -1
            A.extend([k] * (v >> 1))
            B.extend([k] * (-v >> 1))
        return sum(min(a, b, mn * 2) for a, b in zip(sorted(A), sorted(B, reverse=True)))
    
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.minCost([4,2,2,2], [1,4,1,2]))  # 1
print(sol.minCost([2,3,4,1], [3,2,5,1]))  # -1