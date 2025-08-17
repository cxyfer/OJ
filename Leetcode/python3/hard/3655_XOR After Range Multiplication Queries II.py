#
# @lc app=leetcode id=3655 lang=python3
#
# [3655] XOR After Range Multiplication Queries II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9 + 7)

class Solution1:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q = len(nums), len(queries)
        mp = defaultdict(lambda: defaultdict(list))
        BLK_SZ = int(math.sqrt(q))
        for l, r, k, v in queries:
            if k > BLK_SZ:
                for idx in range(l, r + 1, k):
                    nums[idx] = (nums[idx] * v) % MOD
            else:
                mp[k][l % k].append((l, r, v))

        for k, ms in mp.items():
            for m, lst in ms.items():
                ln = (n - 1 - m) // k + 1
                diff = [1] * (ln + 1)
                for l, r, v in lst:
                    st = (l - m) // k
                    ed = (r - m) // k
                    diff[st] = (diff[st] * v) % MOD
                    diff[ed + 1] = (diff[ed + 1] * pow(v, MOD - 2, MOD)) % MOD
                d = 1
                for i in range(ln):
                    d = d * diff[i] % MOD
                    idx = m + i * k
                    nums[idx] = (nums[idx] * d) % MOD
        return reduce(xor, nums, 0)

class Solution2:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q = len(nums), len(queries)
        BLK_SZ = int(math.sqrt(q))
        mp = defaultdict(lambda : [1] * (n + 1))
        for l, r, k, v in queries:
            if k > BLK_SZ:
                for idx in range(l, r + 1, k):
                    nums[idx] = (nums[idx] * v) % MOD
            else:
                m = l % k
                r = ((r - m) // k + 1) * k + m
                mp[k][l] = mp[k][l] * v % MOD
                if r < n:
                    mp[k][r] = mp[k][r] * pow(v, MOD - 2, MOD) % MOD
        for k in mp.keys():
            for m in range(k):
                d = 1
                for i in range(m, n, k):
                    d = d * mp[k][i] % MOD
                    nums[i] = nums[i] * d % MOD
        return reduce(xor, nums, 0)

Solution = Solution1    
# Solution = Solution2
# @lc code=end


sol = Solution()
print(sol.xorAfterQueries([1, 1, 1], [[0, 2, 1, 4]]))  # 4
print(sol.xorAfterQueries([2, 3, 1, 5, 4], [[1, 4, 2, 3], [0, 2, 1, 2]]))  # 31   