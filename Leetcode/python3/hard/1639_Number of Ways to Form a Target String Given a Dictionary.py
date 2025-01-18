#
# @lc app=leetcode id=1639 lang=python3
# @lcpr version=30204
#
# [1639] Number of Ways to Form a Target String Given a Dictionary
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:  
    def numWays(self, words: List[str], target: str) -> int:  
        MOD = 10 ** 9 + 7
        m = len(words[0]);n = len(target)
        cnt = [defaultdict(int) for _ in range(m)]
        for word in words:
            for i, ch in enumerate(word):
                cnt[i][ch] += 1

        @cache
        def dfs(i: int, j: int) -> int:
            if j == -1:
                return 1
            if i == -1:
                return 0
            return (dfs(i - 1, j) + cnt[i][target[j]] * dfs(i - 1, j - 1)) % MOD
        return dfs(m - 1,n - 1)
# @lc code=end
solution = Solution()  
print(solution.numWays(["acca","bbbb","caca"], "aba"))  # 輸出: 6  
print(solution.numWays(["abba", "baab"], "bab"))  # 輸出: 4

#
# @lcpr case=start
# ["acca","bbbb","caca"]\n"aba"\n
# @lcpr case=end

# @lcpr case=start
# ["abba","baab"]\n"bab"\n
# @lcpr case=end

#

