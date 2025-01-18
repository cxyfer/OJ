# @algorithm @lc id=2025 lang=python3 
# @title redistribute-characters-to-make-all-strings-equal


from en.Python3.mod.preImport import *
# @test(["abc","aabc","bc"])=true
# @test(["ab","a"])=false
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        cnt = Counter([ch for word in words for ch in word])
        return all(v % n == 0 for v in cnt.values())