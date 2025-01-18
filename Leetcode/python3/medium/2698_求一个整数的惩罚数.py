#
# @lc app=leetcode.cn id=2698 lang=python3
#
# [2698] 求一个整数的惩罚数
#

# @lc code=start
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
# @lc code=end

