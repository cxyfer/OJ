#
# @lc app=leetcode id=2326 lang=python3
# @lcpr version=30204
#
# [2326] Spiral Matrix IV
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
    """
        Simulation
        從左上角開始，按照順時針方向依次填入數字，遇到邊界或已經填過的數字就轉向
    """
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 定義四個方向
        ans = [[-1] * n for _ in range(m)] # 初始化答案矩陣
        x, y, cd = 0, 0, 0 # 初始化起始位置和方向
        while head is not None:
            ans[x][y] = head.val # 填入數字
            head = head.next # 移動到鏈接串列的下一個節點
            nx, ny = x + DIR[cd][0], y + DIR[cd][1] # 計算新位置
            # 若新位置超出邊界或已經填過，則需要轉向
            if (nx < 0 or nx >= m or ny < 0 or ny >= n or ans[nx][ny] != -1):
                cd = (cd + 1) % 4 # 轉向
                nx, ny = x + DIR[cd][0], y + DIR[cd][1] # 計算新位置
            x, y = nx, ny # 更新位置
        return ans
# @lc code=end


#
# @lcpr case=start
# 3\n5\n[3,0,2,6,8,1,7,9,4,2,5,5,0]\n
# @lcpr case=end

# @lcpr case=start
# 1\n4\n[0,1,2]\n
# @lcpr case=end

#

