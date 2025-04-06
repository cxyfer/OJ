3#
# @lc app=leetcode id=3508 lang=python3
#
# [3508] Implement Router
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Router:

    def __init__(self, memoryLimit: int):
        self.size = memoryLimit
        self.packets = deque()
        self.set = set()
        self.mp = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.set:
            return False
        self.set.add((source, destination, timestamp))
        self.packets.append((source, destination, timestamp))
        self.mp[destination].append((timestamp, source))
        if len(self.packets) > self.size:
            self.forwardPacket()
        return True

    def forwardPacket(self) -> List[int]:
        if not self.packets:
            return []
        s, d, t = self.packets.popleft()
        self.set.remove((s, d, t))
        self.mp[d].popleft()
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        idx1 = bisect_left(self.mp[destination], (startTime, 0))
        idx2 = bisect_right(self.mp[destination], (endTime, float('inf')))
        return idx2 - idx1
# @lc code=end

router = Router(3)
print(router.addPacket(1, 4, 90)) # True
print(router.addPacket(2, 5, 90)) # True
print(router.addPacket(1, 4, 90)) # False
print(router.addPacket(3, 5, 95)) # True  
print(router.addPacket(4, 5, 105)) # True
print(router.forwardPacket()) # [2, 5, 90]
print(router.addPacket(5, 2, 110)) # True
print(router.getCount(5, 100, 110)) # 1