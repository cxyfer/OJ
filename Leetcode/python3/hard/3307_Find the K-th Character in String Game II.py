#
# @lc app=leetcode id=3307 lang=python3
#
# [3307] Find the K-th Character in String Game II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1a:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def f(k: int) -> int:
            if k == 1:
                return 0
            m = (k - 1).bit_length()
            if k < (1 << (m - 1)):
                return f(k)
            else:
                return operations[m - 1] + f(k - (1 << (m - 1)))
        return chr(ord('a') + f(k) % 26)
    
class Solution1b:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        m = (k - 1).bit_length()
        cnt = 0
        for i in range(m - 1, -1, -1):
            if k > (1 << i):
                k -= (1 << i)
                cnt += operations[i]
        return chr(ord('a') + cnt % 26)
    
class Solution2:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        m = (k - 1).bit_length()
        mask = reduce(lambda x, y: x | y, [1 << i for i, b in enumerate(operations[:m]) if b], 0)
        return chr(ord('a') + ((k - 1) & mask).bit_count() % 26)

# Solution = Solution1a
# Solution = Solution1b
Solution = Solution2
# @lc code=end
sol = Solution()
print(sol.kthCharacter(5, [0,0,0]))  # 'a`
print(sol.kthCharacter(10, [0,1,0,1]))  # 'b
print(sol.kthCharacter(1, [0]))  # 'a'