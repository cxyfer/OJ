# @algorithm @lc id=2573 lang=python3 
# @title remove-nodes-from-linked-list


from en.Python3.mod.preImport import *
# @test([5,2,13,3,8])=[13,8]
# @test([1,1,1,1])=[1,1,1,1]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        node = self.removeNodes(head.next) # 剩下裡面最大的
        if node.val > head.val: # 刪除 head
            return node
        head.next = node # 不刪除 head
        return head

            
        