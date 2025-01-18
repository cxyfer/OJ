# @algorithm @lc id=38 lang=python3 
# @title count-and-say


from en.Python3.mod.preImport import *
# @test(1)="1"
# @test(4)="1211"
class Solution:
    def countAndSay(self, n: int) -> str:
            def say(s):
                n = len(s)
                res = ""
                i = 0
                while i < n:
                    j = i + 1
                    while j < n and s[j] == s[i]: # 找到下一個不同的數字
                        j += 1
                    res += str(j-i) + s[i]
                    i = j
                return res
            
            s = "1"
            for _ in range(n-1):
                s = say(s)
            return s