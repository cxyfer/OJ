# @algorithm @lc id=234 lang=python3 
# @title palindrome-linked-list


from en.Python3.mod.preImport import *
# @test([1,2,2,1])=true
# @test([1,2])=false
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst == lst[::-1]