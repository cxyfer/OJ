#
# @lc app=leetcode.cn id=2337 lang=python3
#
# [2337] 移动片段得到字符串
#

# @lc code=start
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Two pointers
        if len(start) != len(target):
            return False
        if start == target:
            return True
        if start.replace("_","") != target.replace("_", ""):
            return False
        n = len(start)
        i = j = 0 # pointer for L and R
        while (1):
            while i < n and start[i] == "_":
                i += 1
            while j < n and target[j] == "_":
                j += 1
            if i >= n and j >= n:
                return True
            # 因為前面已經確認過 start.replace("_","") == target.replace("_", "")
            # 所以當 start[i] != "_" 且target[j] != "_" 時，兩者必定相等
            if (start[i] == 'L' and i < j) or (start[i] == 'R' and i > j):
                return False
            i += 1
            j += 1
        return True

# @lc code=end

