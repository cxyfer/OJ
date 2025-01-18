# @algorithm @lc id=451 lang=python3 
# @title sort-characters-by-frequency


from en.Python3.mod.preImport import *
# @test("tree")="eert"
# @test("cccaaa")="aaaccc"
# @test("Aabb")="bbAa"
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        ans = ""
        for k, v in sorted(cnt.items(), key=lambda x: -x[1]):
            ans += k * v
        return ans