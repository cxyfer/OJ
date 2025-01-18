# @algorithm @lc id=2727 lang=python3 
# @title number-of-senior-citizens


from en.Python3.mod.preImport import *
# @test(["7868190130M7522","5303914400F9211","9273338290F4010"])=2
# @test(["1313579440F2036","2921522980M5644"])=0
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                ans += 1
        return ans