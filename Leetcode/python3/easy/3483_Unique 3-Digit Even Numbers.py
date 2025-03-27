#
# @lc app=leetcode id=3483 lang=python3
#
# [3483] Unique 3-Digit Even Numbers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()
        for (x, y, z) in permutations(digits, 3):
            if x == 0 or z & 1: continue
            ans.add(x * 100 + y * 10 + z)
        return len(ans)

class Solution2:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = 0
        cnt = [0] * 10
        for x in digits:
            cnt[x] += 1
        for x in range(1, 10):
            if cnt[x] == 0: continue
            cnt[x] -= 1
            for y in range(10):
                if cnt[y] == 0: continue
                cnt[y] -= 1
                for z in range(0, 10, 2):
                    if cnt[z] == 0: continue
                    ans += 1
                cnt[y] += 1
            cnt[x] += 1
        return ans
    
# Solution = Solution1
Solution = Solution2
# @lc code=end
