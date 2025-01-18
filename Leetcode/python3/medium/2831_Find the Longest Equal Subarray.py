#
# @lc app=leetcode id=2831 lang=python3
# @lcpr version=30202
#
# [2831] Find the Longest Equal Subarray
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Sliding window
        
        首先紀錄每個元素出現的位置，pos[x] 為元素 x 出現的位置列表，列表中的元素為該元素在原陣列中的下標。
        接著枚舉每個元素 x ，以該元素為窗口的左右邊界，根據題意，窗口內最多只有 k 個元素與當前枚舉的元素 x 不同
        令 left, right 為窗口的左右邊界，指向 pos[x] 之下標
        - 則 pos[x][right] - pos[x][left] + 1 為目前窗口在原陣列中的長度
        - right - left + 1 為目前窗口內元素 x 的數量
        - 兩者相減，即為窗口內非 x 元素的數量，也就是需要刪除的元素數量
    """
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pos = defaultdict(list) # 紀錄每個元素出現的位置
        for i, x in enumerate(nums):
            pos[x].append(i)
        ans = 0
        for x, lst in pos.items(): 
            left = 0 # left, right 為窗口的左右邊界，是 pos[x] 中的下標
            for right, idx in enumerate(lst):
                while (idx - lst[left] + 1) - (right - left + 1) > k: # 若不符合條件，則開始縮小窗口
                    left += 1
                ans = max(ans, right - left + 1) # 更新答案
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,3,2,3,1,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,2,1,1]\n2\n
# @lcpr case=end

#

