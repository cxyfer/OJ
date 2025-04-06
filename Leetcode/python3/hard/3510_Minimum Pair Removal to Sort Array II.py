#
# @lc app=leetcode id=3510 lang=python3
#
# [3510] Minimum Pair Removal to Sort Array II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Node:
    def __init__(self, val: int, idx: int):
        self.val = val
        self.idx = idx
        self.prev = None
        self.next = None
        self.flag = True

    def __lt__(self, other):
        return (self.val, self.idx) < (other.val, other.idx)
        
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        
        cnt = sum(x > y for x, y in pairwise(nums))
        if cnt == 0:
            return 0
        
        nodes = [Node(val, i) for i, val in enumerate(nums)]
        hp = []
        for i, (x, y) in enumerate(pairwise(nodes)):
            x.next = y
            y.prev = x
            heappush(hp, (x.val + y.val, i, x, y))
        
        ans = 0
        while cnt > 0:
            while hp:
                _, _, x, y = heappop(hp)
                if (x.flag and y.flag and x.next == y):
                    break

            x.flag = y.flag = False

            cur = Node(x.val + y.val, x.idx)
            pre = x.prev
            nxt = y.next
            cur.prev = pre
            cur.next = nxt
            if pre:
                pre.next = cur
            if nxt:
                nxt.prev = cur

            if pre:
                cnt += ((pre.val > cur.val) - (pre.val > x.val))
            cnt -= (x.val > y.val)
            if nxt:
                cnt += ((cur.val > nxt.val) - (y.val > nxt.val))
            
            ans += 1
            if pre:
                heappush(hp, (pre.val + cur.val, pre.idx, pre, cur))
            if nxt:
                heappush(hp, (cur.val + nxt.val, cur.idx, cur, nxt))
                
        return ans
# @lc code=end
sol = Solution()
print(sol.minimumPairRemoval([5,2,3,1]))  # 2
print(sol.minimumPairRemoval([1,2,2]))  # 0
print(sol.minimumPairRemoval([2,2,-1,3,-2,2,1,1,1,0,-1]))  # 9
