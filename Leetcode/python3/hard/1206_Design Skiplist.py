#
# @lc app=leetcode id=1206 lang=python3
# @lcpr version=30202
#
# [1206] Design Skiplist
#


# @lcpr-template-start
from preImport import *
import random
# @lcpr-template-end
# @lc code=start
class Node:
    def __init__(self, val=-1, next=None, down=None):
        self.val = val
        self.next = next
        self.down = down

class Skiplist:
    def __init__(self, max_lvl=20, p=0.5):
        self.head = Node()  # 最高層的 dummy node
        self.MAX_LVL = max_lvl  # max level
        self.P = p  # 向上傳遞的機率
    
    # 隨機決定新節點的層數
    def get_random_level(self):
        lvl = 1
        while random.random() < self.P and lvl < self.MAX_LVL:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            # 在當前層向右移動直到找到第一個不小於目標值的節點
            while curr.next and curr.next.val < target:
                curr = curr.next
            if curr.next and curr.next.val == target:
                return True
            # 如果找不到目標值，則向下移動
            curr = curr.down
        return False

    def add(self, num: int) -> None:
        st = []  # 記錄每一層需要插入的位置
        curr = self.head
        
        # 找到每一層可能需要插入的位置
        while curr:
            while curr.next and curr.next.val < num:
                curr = curr.next
            st.append(curr)
            curr = curr.down
            
        # 隨機決定新節點的層數
        level = self.get_random_level()
        down = None
        
        # 從下到上，在選定的層創建新節點並向下移動
        while level > 0 and st:
            prev = st.pop()
            new_node = Node(num, prev.next, down)
            prev.next = new_node
            down = new_node
            level -= 1
            
        # # 如果需要更多層，創建新的層
        while level > 0:
            new_node = Node(num, None, down)
            self.head = Node(-1, new_node, self.head)
            down = new_node
            level -= 1

    def erase(self, num: int) -> bool:
        curr = self.head
        res = False
        
        while curr:
            # 在當前層向右移動
            while curr.next and curr.next.val < num:
                curr = curr.next
            # 如果找到目標值，刪除它
            if curr.next and curr.next.val == num:
                curr.next = curr.next.next
                res = True  # 注意找到目標值後，仍需要繼續向下移動
            # 向下移動
            curr = curr.down
            
        return res
# @lc code=end

obj = Skiplist()
obj.add(1)
obj.add(2)
obj.add(3)
print(obj.search(0))  # False
obj.add(4)
print(obj.search(1))  # True
print(obj.erase(0))  # False
print(obj.erase(1))  # True
print(obj.search(1))  # False