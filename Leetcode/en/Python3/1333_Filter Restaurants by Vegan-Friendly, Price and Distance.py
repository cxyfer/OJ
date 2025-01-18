# @algorithm @lc id=1455 lang=python3 
# @title filter-restaurants-by-vegan-friendly-price-and-distance


from en.Python3.mod.preImport import *
# @test([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],1,50,10)=[3,1,5]
# @test([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],0,50,10)=[4,3,2,1,5]
# @test([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],0,30,3)=[4,5]
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        # restaurants.sort(key=lambda x:(x[1], x[0]), reverse=True)
        restaurants.sort(key=lambda x: (-x[1], -x[0]))
        return [x[0] for x in restaurants if x[2] >= veganFriendly and x[3] <= maxPrice and x[4] <= maxDistance]