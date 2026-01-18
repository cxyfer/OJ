#
# @lc app=leetcode id=3815 lang=python3
#
# [3815] Design Auction System
#


# @lcpr-template-start
from preImport import *
from heapq import heappush_max, heappop_max
# @lcpr-template-end
# @lc code=start
class AuctionSystem:

    def __init__(self):
        self.record = defaultdict(dict)  # itemId -> userId -> bidAmount
        self.item_h = defaultdict(list)  # itemId -> (bidAmount, userId)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.record[itemId][userId] = bidAmount
        heappush_max(self.item_h[itemId], (bidAmount, userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.record[itemId][userId] = newAmount
        heappush_max(self.item_h[itemId], (newAmount, userId))

    def removeBid(self, userId: int, itemId: int) -> None:
        self.record[itemId][userId] = 0

    def getHighestBidder(self, itemId: int) -> int:
        hp = self.item_h[itemId]
        mp = self.record[itemId]
        # Lazy deletion
        while hp and hp[0][0] != mp[hp[0][1]]:
            heappop_max(hp)
        return hp[0][1] if hp else -1
# @lc code=end

obj = AuctionSystem()
obj.addBid(1, 7, 5)
obj.addBid(2, 7, 6)
print(obj.getHighestBidder(7)) # 2
obj.updateBid(1, 7, 8)
print(obj.getHighestBidder(7)) # 1
obj.removeBid(2, 7)
print(obj.getHighestBidder(7)) # 1
print(obj.getHighestBidder(3)) # -1