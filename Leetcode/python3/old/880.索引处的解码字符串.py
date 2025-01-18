#
# @lc app=leetcode.cn id=880 lang=python3
#
# [880] 索引处的解码字符串
#

# @lc code=start
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0 # length of decoded string
        for ch in s:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1
        for ch in reversed(s): # 由後往前，縮減長度
            k %= size
            if k == 0 and ch.isalpha():
                return ch
            if ch.isdigit(): # 前面的字串重複int(ch)次，所以長度可以縮減int(ch)倍
                size //= int(ch)
            else:
                size -= 1


# @lc code=end
sol = Solution()
print(sol.decodeAtIndex("leet2code3",10)) # "o"
print(sol.decodeAtIndex("ha22",5)) # "h"
print(sol.decodeAtIndex("a2345678999999999999999", 1)) # "a"

