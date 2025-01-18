#
# @lc app=leetcode id=725 lang=python3
# @lcpr version=30204
#
# [725] Split Linked List in Parts
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 計算 LinkedList 的長度 cnt
        cnt = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            cnt += 1
        # 將長度為 cnt 分割為 k 個部分，前 r 個部分大小為 q + 1、後 k - r 個部分大小為 q  
        q, r = divmod(cnt, k)

        # 初始化答案
        ans = [None] * k
        
        # 依照前述的大小，填充每一個部份
        idx = 0
        cur = head
        while (idx < k and cur):
            ans[idx] = cur # type: ignore
            # 走完每個部分的長度
            sz = q + (1 if idx < r else 0)
            for _ in range(sz - 1):
                cur = cur.next
            # 斷開上一段與下一段
            nxt = cur.next
            cur.next = None
            cur = nxt
            idx += 1
        return ans
# @lc code=end

#
# @lcpr case=start
# [1,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7,8,9,10]\n3\n
# @lcpr case=end

#

