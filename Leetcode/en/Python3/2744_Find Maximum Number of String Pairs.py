# @algorithm @lc id=2847 lang=python3 
# @title find-maximum-number-of-string-pairs


from en.Python3.mod.preImport import *
# @test(["cd","ac","dc","ca","zz"])=2
# @test(["ab","ba","cc"])=1
# @test(["aa","ab"])=0
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        cnt = Counter()
        for w in words:
            ans += cnt[w]
            cnt[w[::-1]] += 1
        return ans