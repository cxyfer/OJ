#
# @lc app=leetcode id=3885 lang=python3
#
# [3885] Design Event Manager
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class EventManager:
    def __init__(self, events: list[list[int]]):
        self.hp = []
        self.mp = defaultdict(lambda: -1)
        for event_id, priority in events:
            self.mp[event_id] = priority
            self.hp.append((-priority, event_id))
        heapify(self.hp)

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.mp[eventId] = newPriority
        heappush(self.hp, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.hp:
            priority, event_id = heappop(self.hp)
            if self.mp[event_id] == -priority:
                del self.mp[event_id]
                return event_id
        return -1

# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()
# @lc code=end

