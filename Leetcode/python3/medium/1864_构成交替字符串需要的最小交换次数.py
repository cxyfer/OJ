#
# @lc app=leetcode.cn id=1864 lang=python3
#
# [1864] 构成交替字符串需要的最小交换次数
#

# @lc code=start
class Solution:
    """
        只有兩種情況: 010101... or 101010...
        分別計算兩種情況的交換次數, 取最小值
    """
    def minSwaps(self, s: str) -> int:
        n = len(s)
        cnt0_0 = cnt0_1 = 0 # 010101... 0->1, 1->0
        cnt1_0 = cnt1_1 = 0 # 101010... 0->1, 1->0
        for idx, ch in enumerate(s):
            if idx % 2 == 0:
                if ch == '0':
                    cnt1_0 += 1 # '1'01010... 0->1
                else:
                    cnt0_1 += 1 # '0'10101... 1->0
            else:
                if ch == '0':
                    cnt0_0 += 1 # 0'1'0101... 0->1
                else:
                    cnt1_1 += 1 # 1'0'1010... 1->0
        if cnt0_0 == cnt0_1 and cnt1_0 == cnt1_1:
            return min(cnt0_0, cnt1_0)
        elif cnt0_0 == cnt0_1:
            return cnt0_0
        elif cnt1_0 == cnt1_1:
            return cnt1_0
        else:
            return -1
# @lc code=end

