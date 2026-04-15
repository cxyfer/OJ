#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x: str, y: str) -> int:
            xy = x + y
            yx = y + x
            if xy < yx:
                return 1
            elif xy > yx:
                return -1
            else:
                return 0

        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(cmp))
        return "".join(nums) if nums[0] != "0" else "0"


class Solution2:
    def largestNumber(self, nums: List[int]) -> str:
        """
        來自 abc434_f 的神奇技巧
        在該題使用 cmp_to_key 會超時，但使用 class 的 __lt__ 方法實現字串排序不會
        https://atcoder.jp/contests/abc434/tasks/abc434_f
        """
        class C(str):
            def __lt__(self, other: str) -> bool:
                return self + other < other + self

        nums = list(map(str, nums))
        nums.sort(key=C, reverse=True)
        return "".join(nums) if nums[0] != "0" else "0"


# Solution = Solution1
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.largestNumber([10, 2]))