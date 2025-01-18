# @algorithm @lc id=138 lang=python3 
# @title copy-list-with-random-pointer


from en.Python3.mod.preImport import *
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
# @test([[7,null],[13,0],[11,4],[10,2],[1,0]])=[[7,null],[13,0],[11,4],[10,2],[1,0]]
# @test([[1,1],[2,1]])=[[1,1],[2,1]]
# @test([[3,null],[3,0],[3,null]])=[[3,null],[3,0],[3,null]]
class Solution:
    """
        Hash Table
        這題的關鍵在於如何處理random指針，因為random指針可能指向後面還沒創立的節點，所以不能直接從頭開始遍歷。
        因此在遇到還沒創立的節點時，先創立一個新節點，並將其存入hash table中，以便後續使用。
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hash_table = {}

        def check_and_create(node): # 檢查節點是否已經存在，若不存在則創立一個新節點
            if not node:
                return None
            if node not in hash_table:
                hash_table[node] = Node(node.val)
            return hash_table[node]
        
        cur = head 
        while cur:
            new = check_and_create(cur)
            if cur.next:
                new.next = check_and_create(cur.next)
            if cur.random:
                new.random = check_and_create(cur.random)
            cur = cur.next
        return hash_table[head]