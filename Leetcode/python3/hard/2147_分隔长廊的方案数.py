#
# @lc app=leetcode.cn id=2147 lang=python3
#
# [2147] 分隔长廊的方案数
#

# @lc code=start
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        ans = 1
        cnt_s = 0 
        last = 0 
        for i, ch in enumerate(corridor):
            if ch == 'S':
                cnt_s += 1
                # 對於 第3,5,7,... 個座位，可以在其到其左側最近座位之間的任意一個位置放置屏風
                if cnt_s >= 3 and cnt_s % 2:
                    ans = (ans * (i - last)) % MOD 
                last = i # 上一個座位的位置
        # 存在座位是0個或者奇數個的情況，此時方案數為0
        return 0 if cnt_s == 0 or cnt_s % 2 != 0 else ans
# @lc code=end

