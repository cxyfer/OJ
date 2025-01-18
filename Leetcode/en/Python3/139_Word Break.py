# @algorithm @lc id=139 lang=python3 
# @title word-break


from en.Python3.mod.preImport import *
# @test("leetcode",["leet","code"])=true
# @test("applepenapple",["apple","pen"])=true
# @test("catsandog",["cats","dog","sand","and","cat"])=false
class Solution:
    """
        Dynamic Programming
        dp[i] 表示s[:i]是否可以被拆分
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict) # O(1) for lookup
        max_len = max([len(w) for w in wordDict]) # for pruning
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(max(0, i-max_len), i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]