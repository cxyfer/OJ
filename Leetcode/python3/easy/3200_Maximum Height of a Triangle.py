#
# @lc app=leetcode id=3200 lang=python3
# @lcpr version=30204
#
# [3200] Maximum Height of a Triangle
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def check(x: int, y: int) -> int:
            cur = 1
            while x > 0 or y > 0:
                if cur & 1: # odd
                    if x >= cur:
                        x -= cur
                    else:
                        break
                else: # even
                    if y >= cur:
                        y -= cur
                    else:
                        break
                cur += 1
            return cur - 1
        return max(check(red, blue), check(blue, red))

class Solution2:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def check(x: int, y: int) -> int:
            """
                (1 + 3 + 5 + ... + 2 * t1 - 1) <= x
                (2 + 4 + 6 + ... + 2 * t2) <= y

                (1 + 2 * t1 - 1) * t1 / 2 <= x
                t1 * t1 <= x
                t1 = floor(sqrt(x))

                (2 + 2 * t2) * t2 / 2 <= y
                t2 * (t2 + 1) <= y
                t2^2 + t2 - y <= 0
                t2 <= (-1 + sqrt(1 + 4 * y)) / 2
            """
            t1 = int(math.sqrt(x))
            t2 = int((-1 + math.sqrt(1 + 4 * y)) / 2)
            return t2 * 2 + 1 if t1 > t2 else t1 * 2
        return max(check(red, blue), check(blue, red))
    
class Solution(Solution1):
# class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()


#
# @lcpr case=start
# 2\n4\n
# @lcpr case=end

# @lcpr case=start
# 2\n1\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

# @lcpr case=start
# 10\n1\n
# @lcpr case=end

#

