#
# @lc app=leetcode.cn id=2353 lang=python3
# @lcpr version=30204
#
# [2353] 设计食物评分系统
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Heap with lazy update
2. SortedSet
"""
# @lc code=start
class FoodRatings1:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.fd = defaultdict(int)  # food -> (cuisine, rating)
        self.cs = defaultdict(list) # cuisine -> max heap of (-rating, food)
        for f, c, r in zip(foods, cuisines, ratings):
            self.fd[f] = (c, r)
            self.cs[c].append((-r, f))
        for c in self.cs:
            heapify(self.cs[c])

    def changeRating(self, food: str, newRating: int) -> None:
        c, r = self.fd[food]
        heappush(self.cs[c], (-newRating, food))  # Lazy update
        self.fd[food] = (c, newRating)

    def highestRated(self, cuisine: str) -> str:
        hp = self.cs[cuisine]
        while -hp[0][0] != self.fd[hp[0][1]][1]:  # Lazy update
            heappop(hp)
        return hp[0][1]

from sortedcontainers import SortedSet

class FoodRatings2:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.fd = dict()
        self.cs = defaultdict(lambda: SortedSet([], key=lambda x: (-x[1], x[0])))
        for f, c, r in zip(foods, cuisines, ratings):
            self.fd[f] = (c, r)
            self.cs[c].add((f, r))

    def changeRating(self, food: str, newRating: int) -> None:
        c, r = self.fd[food]
        self.cs[c].remove((food, r))
        self.cs[c].add((food, newRating))
        self.fd[food] = (c, newRating)

    def highestRated(self, cuisine: str) -> str:
        return self.cs[cuisine][0][0]

class FoodRatings(FoodRatings1):
    pass

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
# @lc code=end



