# @algorithm @lc id=2802 lang=python3 
# @title find-the-punishment-number-of-an-integer


from en.Python3.mod.preImport import *
# @test(10)=182
# @test(37)=1478

ANS = [0] * 1001
for i in range(1, 1001):
    s = str(i * i) # convert to string
    n = len(s)
    def check(p: int, sum: int) -> bool: # recursive
        if p == n: # recursion end
            return sum == i
        x = 0 # sum of substring
        for j in range(p, n): 
            x = x * 10 + int(s[j])
            if check(j + 1, sum + x):
                return True
        return False
    ANS[i] = ANS[i - 1] + (i * i if check(0, 0) else 0)

class Solution:
    def punishmentNumber(self, n: int) -> int:
        return ANS[n]