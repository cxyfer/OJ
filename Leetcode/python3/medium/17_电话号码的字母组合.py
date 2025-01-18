#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
from preImport import *
# @lc code=start
class Solution:
    """
        Backtrace, similar to 46.Permutations.
        Time Complexity: O(N * 4^N)
        Space Complexity: O(N)
    """
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        MAPPING = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno',7:'pqrs', 8: 'tuv', 9: 'wxyz'}
        ans = []
        path = []
        def dfs(i: int) -> None:
            if i == n:
                ans.append(''.join(path))
                return
            for ch in MAPPING[int(digits[i])]:
                path.append(ch)
                dfs(i + 1)
                path.pop()
        dfs(0)
        return ans
# @lc code=end

