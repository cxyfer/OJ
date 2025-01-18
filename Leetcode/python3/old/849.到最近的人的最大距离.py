#
# @lc app=leetcode.cn id=849 lang=python3
#
# [849] 到最近的人的最大距离
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        ans = 0
        l = 0
        for idx in range(n):
            if seats[idx] == 1:
                if l == 0 and seats[0] == 0: # if leftmost seat is empty
                    ans = idx
                ans = max(ans, (idx-l)//2) # middle seat
                l = idx # Updata left seat index
        if seats[n-1] == 0:
            ans = max(ans, n - 1 - l ) # if rightmost seat is empty
        return ans
           

# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    # print(sol.maxDistToClosest([1,0,0,0,1,0,1])) # 2
    # print(sol.maxDistToClosest([1,0,0,0])) # 3
    # print(sol.maxDistToClosest([0,1,0,1,0])) # 1
    # print(sol.maxDistToClosest([0,1])) # 1
    print(sol.maxDistToClosest([1,0,0,0,1,0,1])) # 2
