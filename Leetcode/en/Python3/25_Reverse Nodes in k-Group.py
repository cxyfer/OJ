# @algorithm @lc id=25 lang=python3 
# @title reverse-nodes-in-k-group


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5],2)=[2,1,4,3,5]
# @test([1,2,3,4,5],3)=[3,2,1,4,5]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
        Advanced version of 92. Reverse Linked List II
    """
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        tmp = head
        while tmp:
            n += 1
            tmp = tmp.next

        dummy = ListNode(next=head)
        p0 = dummy # 上一段的結尾

        while(n >= k):
            n -= k
            pre = None
            cur = p0.next # 從上一段的結尾後一個開始
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            last = p0.next # 這一段的結尾(原本的開頭)
            p0.next.next = cur # 下一段的開頭
            p0.next = pre # 這一段的開頭(原本的結尾)
            p0 = last 
        return dummy.next