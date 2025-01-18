# @algorithm @lc id=17 lang=python3 
# @title letter-combinations-of-a-phone-number


from en.Python3.mod.preImport import *
# @test("23")=["ad","ae","af","bd","be","bf","cd","ce","cf"]
# @test("")=[]
# @test("2")=["a","b","c"]
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
            Backtrace, similar to 46.Permutations.
            Time Complexity: O(N * 4^N)
            Space Complexity: O(N)
        """
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
            for c in MAPPING[int(digits[i])]:
                path.append(c)
                dfs(i + 1)
                path.pop()
        dfs(0)
        return ans
