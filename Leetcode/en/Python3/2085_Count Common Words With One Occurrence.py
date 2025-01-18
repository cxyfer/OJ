# @algorithm @lc id=2190 lang=python3 
# @title count-common-words-with-one-occurrence


from en.Python3.mod.preImport import *
# @test(["leetcode","is","amazing","as","is"],["amazing","leetcode","is"])=2
# @test(["b","bb","bbb"],["a","aa","aaa"])=0
# @test(["a","ab"],["a","a","a","ab"])=1
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt1 = Counter(words1)
        cnt2 = Counter(words2)
        cnt = Counter()
        for k, v in cnt1.items():
            if v == 1:
                cnt[k] += 1
        for k, v in cnt2.items():
            if v == 1:
                cnt[k] += 1
        return len([k for k, v in cnt.items() if v == 2])