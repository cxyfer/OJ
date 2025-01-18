# 8022. Find the Minimum Possible Sum of a Beautiful Array
# You are given positive integers n and target.

# An array nums is beautiful if it meets the following conditions:

# nums.length == n.
# nums consists of pairwise distinct positive integers.
# There doesn't exist two distinct indices, i and j, in the range [0, n - 1], such that nums[i] + nums[j] == target.
# Return the minimum possible sum that a beautiful array could have.

from collections import Counter
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        # 長度為n的array，每個數字都是正整數，且兩兩不相同，且任兩個相加不等於target
        # 回傳最小可能的sum
        cnt = Counter()
        res = {}
        s = 0
        l = 0
        for i in range(1, 2*n+1):
            j = target - i # 是否有相加等於target的數字
            if j in res.keys(): # 有的話，就不要加i進去
                continue
            res[i] = True
            s += i
            l += 1
            if l == n: # 長度為n，就可以停止了
                return s

if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumPossibleSum(2, 3)) # 4
    print(sol.minimumPossibleSum(3, 3)) # 8
    print(sol.minimumPossibleSum(1, 1)) # 1