# @algorithm @lc id=109 lang=python3 
# @title convert-sorted-list-to-binary-search-tree


from en.Python3.mod.preImport import *
# @test([-10,-3,0,5,9])=[0,-3,9,-10,null,5]
# @test([])=[]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Similar to 108. Convert Sorted Array to Binary Search Tree
        # Similar to 876. Middle of the Linked List
        # Base case
        if not head: return None
        if not head.next: return TreeNode(head.val)
        # Using fast and slow pointers to find the node of middle node
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if pre:
            pre.next = None # Cut the linked list
        # Recursion
        node = TreeNode(slow.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        return node