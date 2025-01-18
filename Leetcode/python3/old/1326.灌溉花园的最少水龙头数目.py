#
# @lc app=leetcode.cn id=1326 lang=python3
#
# [1326] 灌溉花园的最少水龙头数目
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """
            轉換成造橋問題
            https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden/solutions/2123855/yi-zhang-tu-miao-dong-pythonjavacgo-by-e-wqry/
            Similar to 45. Jump Game II
            Similar to 1024. Video Stitching
        """
        dp = [0] * (n + 1) # dp[i] 表示從前i個水龍頭的可以覆蓋到的最遠距離
        for i, radius in enumerate(ranges): # i表示水龍頭的位置，radius表示水龍頭的半徑
            left = max(0, i - radius) # 水龍頭的左端點
            dp[left] = max(dp[left], i + radius) # 更新左端點可到達的最遠距離

        ams = 0 # 答案
        cur = 0 # 已建造的水龍頭的右端點
        nxt = 0 # 下一座水龍頭的右端點的最大值
        for i in range(n): # 注意不包含n，因為n是終點
            nxt = max(nxt, dp[i])
            if i == cur: # 到達「已」建造的橋的右端點
                if i == nxt: # 到達「可」建造的橋的右端點，即無論怎麼造橋，都無法從i到i+1了
                    return -1
                cur = nxt # 再造一座橋
                ams += 1
        return ams
# @lc code=end

