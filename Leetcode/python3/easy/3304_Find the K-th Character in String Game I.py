#
# @lc app=leetcode id=3304 lang=python3
#
# [3304] Find the K-th Character in String Game I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def kthCharacter(self, k: int) -> str:
        s = "a"
        while len(s) < k:
            s += ''.join([chr(ord('a') + (ord(ch) - ord('a') + 1) % 26) for ch in s])
        return s[k - 1]

class Solution2a:
    def kthCharacter(self, k: int) -> str:
        def f(k: int) -> int:
            if k == 1:
                return 0
            m = (k - 1).bit_length()
            if k < (1 << (m - 1)):
                return f(k)
            else:
                return 1 + f(k - (1 << (m - 1)))
        return chr(ord('a') + f(k))

class Solution2b:
    def kthCharacter(self, k: int) -> str:
        m = (k - 1).bit_length()
        cnt = 0
        for i in range(m - 1, -1, -1):
            if k > (1 << i):
                k -= (1 << i)
                cnt += 1
        return chr(ord('a') + cnt)
    
class Solution2c:
    def kthCharacter(self, k: int) -> str:
        m = (k - 1).bit_length()
        cnt = 0
        for i in range(m - 1, -1, -1):
            # 2b 中的 k > 2^i 等同 k-1 >= 2^i
            # 由於 i 是從大到小，所以當滿足 k-1 >= 2^i 時， (k - 1) >> i 為 1
            if (k - 1) >> i:
                k -= (1 << i)
                cnt += 1
        return chr(ord('a') + cnt)

class Solution3:
    def kthCharacter(self, k: int) -> str:
        # 從 2c 不能發現，實際上是在計算 k-1 的二進制表示中 1 的個數
        return chr(ord('a') + (k - 1).bit_count())

# Solution = Solution1
Solution = Solution2a
# Solution = Solution2b
# Solution = Solution2c
# Solution = Solution3
# @lc code=end


sol = Solution()
print(sol.kthCharacter(5))  # "b"
print(sol.kthCharacter(10))  # "c"
