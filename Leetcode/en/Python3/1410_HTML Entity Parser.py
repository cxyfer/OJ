# @algorithm @lc id=1526 lang=python3 
# @title html-entity-parser


from en.Python3.mod.preImport import *
# @test("&amp; is an HTML entity but &ambassador; is not.")="& is an HTML entity but &ambassador; is not."
# @test("and I quote: &quot;...&quot;")="and I quote: \"...\""
class Solution:
    def entityParser(self, text: str) -> str:
        dic = {
            "&quot;":'"',
            "&apos;":"'",
            "&amp;":"&",
            "&gt;":">",
            "&lt;":"<",
            "&frasl;":"/"
        }
        ans = ""
        tmp = ""
        for ch in text:
            if ch == "&":
                ans += dic[tmp] if tmp and tmp in dic else tmp
                tmp = "&"
            elif ch == ";":
                tmp += ch
                ans += dic[tmp] if tmp and tmp in dic else tmp
                tmp = ""
            else:
                tmp += ch
        ans += tmp
        return ans
        