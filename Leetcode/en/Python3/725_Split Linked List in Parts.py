# @algorithm @lc id=725 lang=python3 
# @title split-linked-list-in-parts


from en.Python3.mod.preImport import *
# @test([1,2,3],5)=[[1],[2],[3],[],[]]
# @test([1,2,3,4,5,6,7,8,9,10],3)=[[1,2,3,4],[5,6,7],[8,9,10]]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 掃描Linked List，得到總長度cnt
        cnt = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            cnt += 1
        # 每個部分的長度
        part, remain = cnt // k, cnt % k
        # 答案，每個部份只需要存head就好
        ans = [ None for _ in range(k)] #
        idx = 0
        cur = head
        while idx < k and cur:
            ans[idx] = cur
            # 每個部分的長度
            size = part + (1 if idx < remain else 0)
            for _ in range(size - 1):
                cur = cur.next
            # 斷開
            next = cur.next
            cur.next = None
            cur = next
            idx += 1
        return ans