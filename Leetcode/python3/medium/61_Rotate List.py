#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Linked List
將 Linked List 形成一個環，接著就只要關注如何找到新的 tail 即可。
"""
# @lc code=start
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        # 計算Linked List的長度
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        # 如果Linked List的長度為1，或者k為0，則直接返回head
        k %= n
        if n == 1 or k == 0:
            return head

        # 將Linked List形成一個環
        tail.next = head

        # 找到新的 tail
        tail = head
        for _ in range(n - k - 1):
            tail = tail.next
        # 由於是環，新的 head 是新的 tail 的下一個節點
        head = tail.next
        # 斷開環
        tail.next = None
        return head
# @lc code=end

