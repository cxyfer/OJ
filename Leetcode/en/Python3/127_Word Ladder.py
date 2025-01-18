# @algorithm @lc id=127 lang=python3 
# @title word-ladder


from en.Python3.mod.preImport import *
# @test("hit","cog",["hot","dot","dog","lot","log","cog"])=5
# @test("hit","cog",["hot","dot","dog","lot","log"])=0
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        