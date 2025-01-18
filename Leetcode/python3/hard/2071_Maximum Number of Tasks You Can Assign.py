#
# @lc app=leetcode id=2071 lang=python3
# @lcpr version=30201
#
# [2071] Maximum Number of Tasks You Can Assign
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Binary Search + Greedy + Deque
        二分檢查是否可以完成 k 個任務，若滿足，則顯然是要求最低的 k 個任務。
        從需求最高的任務開始考慮，貪心思路如下：
            1. 如果有人不吃藥就能完成任務，那麽選擇體力最大的 worker 完成任務。
                因為其一定能完成所有任務，讓他完成要求最高的任務比較划算。
            2. 如果都需要吃藥才能完成任務，那麽選擇體力最小的 worker 吃藥完成任務。
                因為其他 worker 可能可以不吃藥完成要求更低的任務。
        另外用 bisect_left 需要確保 False 在 True 前面，所以 key 要設定為 not check(x)
    """
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        m, n = len(tasks), len(workers)
        tasks.sort()
        workers.sort()
        def check(k): # 檢查是否可以完成要求最低的 k 個任務
            p = pills
            idx = n - 1 # worker
            dq = deque() # 維護吃藥後可以完成當前任務的 worker，由體力大到小排序
            for j in range(k - 1, -1, -1): # task
                while idx >= 0 and workers[idx] + strength >= tasks[j]:
                    dq.append(workers[idx])
                    idx -= 1
                if not dq: # 沒人可以完成當前任務
                    return False
                if dq[0] >= tasks[j]: # 有人不用吃藥，就可以完成當前任務，此時選擇體力最大的 worker
                    dq.popleft()
                else: # deque 中所有人都需要吃藥才能完成當前任務，此時選擇體力最小的 worker
                    if p == 0: # 沒有藥了
                        return False
                    dq.pop()
                    p -= 1
            return True
        return bisect_left(range(0, min(m, n) + 1), True, key = lambda x : not check(x)) - 1 # key 要設定為 not check(x) ，確保 False 在 True 前面
        # left, right = 0, min(m, n)
        # while left <= right:
        #     mid = (left + right) // 2
        #     if check(mid):
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return right # left 是第一個不滿足的，而 right 是最後一個滿足的，所以返回 right
# @lc code=end
sol = Solution()
print(sol.maxTaskAssign([3,2,1], [0,3,3], 1, 1)) # 3
print(sol.maxTaskAssign([5,4], [0,0,0], 1, 5)) # 1
print(sol.maxTaskAssign([10,15,30], [0,10,10,10,10], 3, 10)) # 2
print(sol.maxTaskAssign([35], [83,20,4,66], 3, 41)) # 1

#
# @lcpr case=start
# [3,2,1]\n[0,3,3]\n1\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,4]\n[0,0,0]\n1\n5\n
# @lcpr case=end

# @lcpr case=start
# [10,15,30]\n[0,10,10,10,10]\n3\n10\n
# @lcpr case=end

#

