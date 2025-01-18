# @algorithm @lc id=2235 lang=python3 
# @title capitalize-the-title


from en.Python3.mod.preImport import *
# @test("capiTalIze tHe titLe")="Capitalize The Title"
# @test("First leTTeR of EACH Word")="First Letter of Each Word"
# @test("i lOve leetcode")="i Love Leetcode"
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        for i, w in enumerate(words):
            if len(w) > 2:
                words[i] = w.title()
            else:
                words[i] = w.lower()
        return ' '.join(words)