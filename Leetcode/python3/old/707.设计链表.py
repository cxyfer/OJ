#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.size = 0
        # 這樣寫要處理很多邊界條件
        self.head = None

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val


    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        # Not work when index == 0
        if index > self.size:
            return
        elif index <= 0: 
            self.addAtHead(val)
            return
        
        pre = self.head
        for i in range(index-1):
            pre = pre.next
        
        new_node = Node(val)
        new_node.next = pre.next
        pre.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        else:
            pre = self.head
            for i in range(index-1):
                pre = pre.next
            pre.next = pre.next.next
            self.size -= 1
            return



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

