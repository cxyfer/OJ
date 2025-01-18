3#
# @lc app=leetcode.cn id=1333 lang=python3
#
# [1333] 餐厅过滤器
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        # restaurants.sort(key=lambda x:(x[1], x[0]), reverse=True)
        restaurants.sort(key=lambda x: (-x[1], -x[0]))
        return [x[0] for x in restaurants if x[2] >= veganFriendly and x[3] <= maxPrice and x[4] <= maxDistance]
# @lc code=end
sol = Solution()
print(sol.filterRestaurants([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],1,50,10)) # [3,1,5]
print(sol.filterRestaurants([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],0,50,10)) # [4,3,2,1,5]
print(sol.filterRestaurants([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],0,30,3)) # [4,5]