#
# @lc app=leetcode id=2266 lang=python3
# @lcpr version=30201
#
# [2266] Count Number of Texts
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = 10 ** 9 + 7
MAX_N = 10 ** 5 + 5
dp3 = [1, 1, 2, 4] + [0] * (MAX_N - 4)
dp4 = [1, 1, 2, 4] + [0] * (MAX_N - 4)
for i in range(4, MAX_N):
    dp3[i] = (dp3[i - 1] + dp3[i - 2] + dp3[i - 3]) % MOD
    dp4[i] = (dp4[i - 1] + dp4[i - 2] + dp4[i - 3] + dp4[i - 4]) % MOD
class Solution:
    """
        動態規劃 + 分組循環 + 乘法原理
    """
    def countTexts(self, pressedKeys: str) -> int:
        n = len(pressedKeys)
        ans = 1
        i = 0
        while i < n:
            st = i
            i += 1
            while i < n and pressedKeys[i] == pressedKeys[i - 1]:
                i += 1
            if pressedKeys[i-1] == "7" or pressedKeys[i-1] == "9":
                ans = (ans * dp4[i - st]) % MOD
            else:
                ans = (ans * dp3[i - st]) % MOD
        return ans % MOD
# @lc code=end

sol = Solution()
# print(sol.countTexts("22233")) # 8
# print(sol.countTexts("222222222222222222222222222222222222")) # 82876089
print(sol.countTexts("444479999555588866")) # 3136

#
# @lcpr case=start
# "22233"\n
# @lcpr case=end

# @lcpr case=start
# "222222222222222222222222222222222222"\n
# @lcpr case=end

#

