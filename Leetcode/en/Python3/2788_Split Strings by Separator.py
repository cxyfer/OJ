# @algorithm @lc id=2881 lang=python3 
# @title split-strings-by-separator


from en.Python3.mod.preImport import *
# @test(["one.two.three","four.five","six"],".")=["one","two","three","four","five","six"]
# @test(["$easy$","$problem$"],"$")=["easy","problem"]
# @test(["|||"],"|")=[]
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [x for w in words for x in w.split(separator) if x != '']