#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end

"""
Similar
- 759. Employee Free Time (Premium)
- 2931. Maximum Spending After Buying Items
"""
# @lc code=start
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)

        # 維護一個最小堆，裡面存放每個 list 的當前節點
        hp = []
        for idx, node in enumerate(lists):
            if node is not None:
                heappush(hp, (node.val, idx))

        curr = dummy
        while hp:
            _, idx = heappop(hp)  # pop the smallest node
            node = lists[idx]
            curr.next = node
            curr = curr.next
            if node.next is not None:
                lists[idx] = node.next
                heappush(hp, (node.next.val, idx))
        return dummy.next
# @lc code=end

