#
# @lc app=leetcode id=3592 lang=python3
#
# [3592] Inverse Coin Change
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        ans = []
        f = [1] + [0] * n
        for i, w in enumerate(numWays, 1):
            if w - f[i] == 1:  # 此時意味著存在面額為 i 的硬幣
                ans.append(i)
                for j in range(i, n + 1):
                    f[j] += f[j - i]
            elif w - f[i] != 0:  # 此時說明 numWays 中的值與 f[i] 不匹配
                return []
        return ans
# @lc code=end

sol = Solution()
print(sol.findCoins([0,1,0,2,0,3,0,4,0,5])) # [2,4,6]
print(sol.findCoins([1,2,2,3,4])) # [1,2,5]