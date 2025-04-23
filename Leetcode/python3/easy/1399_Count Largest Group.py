#
# @lc app=leetcode id=1399 lang=python3
#
# [1399] Count Largest Group
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MAX_N = int(1e4 + 5)

def digit(x):
    res = 0
    while x:
        x, r = divmod(x, 10)
        res += r
    return res

mx = 0
cnt = defaultdict(int)
ans = [0] * MAX_N
for n in range(1, MAX_N):
    s = digit(n)
    cnt[s] += 1
    if cnt[s] > mx:
        ans[n] = 1
        mx = cnt[s]
    else:
        ans[n] = ans[n - 1] + (cnt[s] == mx)

class Solution1:
    def countLargestGroup(self, n: int) -> int:
        return ans[n]
    
class Solution2:
    def countLargestGroup(self, n: int) -> int:
        high = list(map(int, str(n)))
        m = len(high)

        @cache
        def dfs(i: int, s: int, limit_high: bool) -> int:
            if i == m:
                return s == 0
            if s == 0: return 1  # 後面只能選 0
            if s < 0: return 0  # 後面選任何數都會超過

            lo = 0
            hi = high[i] if limit_high else 9

            res = 0
            for d in range(lo, hi + 1):
                res += dfs(i + 1, s - d, limit_high and d == hi)
            return res
        
        ans = mx = 0
        for tgt in range(1, 9 * m + 1):
            res = dfs(0, tgt, True)
            if res > mx:
                mx = res
                ans = 1
            elif res == mx:
                ans += 1
        return ans

# Solution = Solution1
Solution = Solution2
# @lc code=end

sol = Solution()
import time
time1 = time.time()
print(sol.countLargestGroup(int(1e50)))
time2 = time.time()
print(time2 - time1)
