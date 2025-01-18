# @algorithm @lc id=3245 lang=python3 
# @title find-beautiful-indices-in-the-given-array-i


from en.Python3.mod.preImport import *
# @test("isawsquirrelnearmysquirrelhouseohmy","my","squirrel",15)=[16,33]
# @test("abcd","a","a",4)=[0]
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        res1, res2 = [], []
        for i in range(n):
            if s[i:].startswith(a):
                res1.append(i)
            if s[i:].startswith(b):
                res2.append(i)
        # Binary Search
        ans = []
        for i in res1:
            j = bisect_left(res2, i)
            if (j < len(res2) and res2[j] - i <= k) or (j > 0 and i - res2[j - 1] <= k):
                ans.append(i)
        return ans