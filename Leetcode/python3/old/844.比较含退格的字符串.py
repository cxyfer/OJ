#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Two pointers from end to starts
        # i,j 分別指向真正要比對的字元，即將可刪除的字元跳過
        i, j = len(s) - 1, len(t) - 1
        # skipS, skipT 分別記錄要跳過的字元數
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    skipS += 1
                elif skipS > 0:
                    skipS -= 1
                else:
                    break
                i -= 1
            while j >= 0:
                if t[j] == "#":
                    skipT += 1
                elif skipT > 0:
                    skipT -= 1
                else:
                    break
                j -= 1
            # 找出真正需要比對的字元後開始比對
            if i >= 0 and j >= 0:
                if s[i] != t[j]: #字元不同
                    return False
            elif (i >= 0 and j < 0) or (i < 0 and j >= 0): # 長度不同
                return False
            i -= 1
            j -= 1
        return True


# @lc code=end

