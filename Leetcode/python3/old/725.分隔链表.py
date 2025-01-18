#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#
from en.Python3.mod.preImport import *
# @lc code=start
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
# @lc code=end

