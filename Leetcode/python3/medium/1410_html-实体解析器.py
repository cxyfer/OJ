#
# @lc app=leetcode.cn id=1410 lang=python3
#
# [1410] HTML 实体解析器
#

# @lc code=start
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
# @lc code=end