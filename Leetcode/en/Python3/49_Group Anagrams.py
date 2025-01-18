# @algorithm @lc id=49 lang=python3 
# @title group-anagrams


from en.Python3.mod.preImport import *
# @test(["eat","tea","tan","ate","nat","bat"])=[["bat"],["nat","tan"],["ate","eat","tea"]]
# @test([""])=[[""]]
# @test(["a"])=[["a"]]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = defaultdict(list)
        for str in strs:
            cnt["".join(sorted(str))].append(str)
        return list(cnt.values())