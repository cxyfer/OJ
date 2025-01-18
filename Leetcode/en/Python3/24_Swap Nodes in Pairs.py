# @algorithm @lc id=24 lang=python3 
# @title swap-nodes-in-pairs


from en.Python3.mod.preImport import *
# @test([1,2,3,4])=[2,1,4,3]
# @test([])=[]
# @test([1])=[1]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.solve1(head)
        # return self.solve2(head)
    """
        1. record 4 node
        p0, (p1, p2), p3 -> p0, (p2, p1), p3
    """
    def solve1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        p0, p1 = dummy, head
        while (p1 and p1.next):
            p2 = p1.next
            p3 = p2.next

            p0.next = p2
            p2.next = p1
            p1.next = p3

            p0 = p1 
            p1 = p3
        return dummy.next
    """
        2. Same as 25. Reverse Nodes in k-Group (k=2)
    """
    def solve2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        k = 2
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