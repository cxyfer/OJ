# @algorithm @lc id=2104 lang=python3 
from en.Python3.mod.preImport import *
# @title operations-on-tree
LOCKED = 0
FREE = 1
class LockingTree:
    def __init__(self, parent: List[int]):
        self.LOCKED = 0
        self.FREE = 1
        self.parents = parent
        self.n = len(parent)
        self.node_state = [(self.FREE, -1) for _ in range(self.n)]
        self.node_childs = defaultdict(list)
        for x, father in enumerate(parent):
            self.node_childs[father].append(x)

    def lock(self, num: int, user: int) -> bool:
        if self.node_state[num][0] == self.LOCKED:
            return False
        else:
            self.node_state[num] = (self.LOCKED, user)
            return True

    def unlock(self, num: int, user: int) -> bool:
        if self.node_state[num] == (self.LOCKED, user):
            self.node_state[num] = (self.FREE, -1)
            return True
        else:
            return False

    def upgrade(self, num: int, user: int) -> bool:
        # 當前節點必需是沒有上鎖的
        if self.node_state[num][0] == self.LOCKED:
            return False
        # 當前節點的祖先節點必需是沒有上鎖的
        p = self.parents[num]
        while p != -1:
            if self.node_state[p][0] == self.LOCKED:
                return False
            p = self.parents[p]
        # 當前節點的子孫節點必需至少有一個是上鎖的
        hasLockedChild = False
        def check(x: int) -> None:
            nonlocal hasLockedChild
            for y in self.node_childs[x]:
                if self.node_state[y][0] == self.LOCKED:
                    hasLockedChild = True
                    break
                check(y)
        check(num)
        if hasLockedChild == False:
            return False
        # 對當前節點上鎖，並且對所有子孫節點解鎖
        self.node_state[num] = (self.LOCKED, user)
        def unlockAllChild(x: int) -> None:
            for y in self.node_childs[x]:
                self.node_state[y] = (self.FREE, -1)
                unlockAllChild(y)
        unlockAllChild(num)
        return True