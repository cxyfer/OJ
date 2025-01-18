#
# @lc app=leetcode.cn id=2353 lang=python3
#
# [2353] 设计食物评分系统
#
from preImport import *
# @lc code=start
from sortedcontainers import SortedSet
class FoodRatings1:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.fd = dict()
        ss = lambda: SortedSet([], key=lambda x: (-x[1], x[0]))
        self.cs = defaultdict(ss)
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
    
class FoodRatings2:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.fd = dict()
        self.cs = defaultdict(list) # Heap
        for f, c, r in zip(foods, cuisines, ratings):
            self.fd[f] = (c, r)
            self.cs[c].append((-r, f))
        for c in self.cs:
            heapq.heapify(self.cs[c])

    def changeRating(self, food: str, newRating: int) -> None:
        c, r = self.fd[food]
        heappush(self.cs[c], (-newRating, food)) # 直接添加，不刪除原本的
        self.fd[food] = (c, newRating)

    def highestRated(self, cuisine: str) -> str:
        hp = self.cs[cuisine]
        while -hp[0][0] != self.fd[hp[0][1]][1]: # 不一樣代表被修改過，直接捨棄
            heappop(hp)
        return hp[0][1]

class FoodRatings(FoodRatings2):
    pass
    
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
# @lc code=end

obj = FoodRatings(foods = ["A","B","C","D","E"], cuisines = ["a","a","a","b","b"], ratings = [3,4,5,1,2])
obj.changeRating(food = "B", newRating = 6)

["FoodRatings","highestRated","highestRated","changeRating","highestRated","changeRating","highestRated"]
[[["kimchi","miso","sushi","moussaka","ramen","bulgogi"],["korean","japanese","japanese","greek","japanese","korean"],[9,12,8,15,14,7]],["korean"],["japanese"],["sushi",16],["japanese"],["ramen",16],["japanese"]]

obj = FoodRatings(foods = ["kimchi","miso","sushi","moussaka","ramen","bulgogi"], cuisines = ["korean","japanese","japanese","greek","japanese","korean"], ratings = [9,12,8,15,14,7])
print(obj.highestRated("korean"))
print(obj.highestRated("japanese"))
obj.changeRating(food = "sushi", newRating = 16)
print(obj.highestRated("japanese"))
obj.changeRating(food = "ramen", newRating = 16)
print(obj.highestRated("japanese")) # ramen