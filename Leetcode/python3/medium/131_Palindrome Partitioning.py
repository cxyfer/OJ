#
# @lc app=leetcode id=131 lang=python3
# @lcpr version=30202
#
# [131] Palindrome Partitioning
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        動態規劃，預處理出所有子字串是否為回文 O(n^2)
        回溯法枚舉所有可能的分割：O(2^n)
    """
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        is_palindrome = [[False] * n for _ in range(n)] # is_palindrome[i][j] is True if s[i:j+1] is palindrome
        for i in range(n):
            is_palindrome[i][i] = True
        for k in range(2, n + 1): # 枚舉長度
            for i in range(n - k + 1): # 枚舉起點
                j = i + k - 1 # 對應的終點
                if s[i] == s[j]: # 頭尾相同，若 長度為2 或 內部也是回文(從 is_palindrome[i+1][j-1] 轉移) ，則是回文
                    if k == 2 or is_palindrome[i + 1][j - 1]:
                        is_palindrome[i][j] = True
                
        ans = []
        path = []
        def dfs(i: int) -> None: # backtracking
            if i == n:
                ans.append(path[:]) # copy path
                return
            for j in range(i, n): # 枚舉終點
                if is_palindrome[i][j]:
                    path.append(s[i:j+1])
                    dfs(j + 1) # 
                    path.pop()
        dfs(0) # 起點從0開始
        return ans
# @lc code=end

sol = Solution()
print(sol.partition("aab")) # [["a","a","b"],["aa","b"]]
print(sol.partition("a")) # [["a"]]

#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#

