#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#
from preImport import *
# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cnt_s = [0] * 10 # 每個數字應該出現的次數
        cnt_g = [0] * 10 # 每個數字實際出現的次數
        x = 0
        for s, g in zip(secret, guess):
            if s == g:
                x += 1
            else:
                cnt_s[int(s)] += 1
                cnt_g[int(g)] += 1
        y = sum([min(cnt_s[i], cnt_g[i]) for i in range(10)])
        return f'{x}A{y}B'
# @lc code=end

