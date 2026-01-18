import math
from typing import *
from collections import *
from functools import *
from heapq import *
from heapq import heappush_max, heappop_max
from bisect import *
from itertools import *
from operator import *

class AuctionSystem:

    def __init__(self):
        self.mp = defaultdict(dict)  # itemId -> userId -> bidAmount
        self.hp = defaultdict(list)  # itemId -> (bidAmount, userId)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.mp[itemId][userId] = bidAmount
        heappush_max(self.hp[itemId], (bidAmount, userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.mp[itemId][userId] = newAmount
        heappush_max(self.hp[itemId], (newAmount, userId))

    def removeBid(self, userId: int, itemId: int) -> None:
        self.mp[itemId][userId] = 0

    def getHighestBidder(self, itemId: int) -> int:
        hp = self.hp[itemId]
        mp = self.mp[itemId]
        while hp and hp[0][0] != mp[hp[0][1]]:
            heappop_max(hp)
        return hp[0][1] if hp else -1

# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)

obj = AuctionSystem()
obj.addBid(1, 7, 5)
obj.addBid(2, 7, 6)
print(obj.getHighestBidder(7)) # 2
obj.updateBid(1, 7, 8)
print(obj.getHighestBidder(7)) # 1
obj.removeBid(2, 7)
print(obj.getHighestBidder(7)) # 1
print(obj.getHighestBidder(3)) # -1