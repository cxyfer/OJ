#
# @lc app=leetcode id=898 lang=python3
#
# [898] Bitwise ORs of Subarrays
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
LogTrick
"""
# @lc code=start
class Solution1a:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans, st = set(), set()
        for x in arr: # 枚舉右端點
            st = {y | x for y in st}
            st.add(x)
            ans.update(st) 
        return len(ans)
    
class Solution1b:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        st = []
        ans = set()
        for x in arr: # 枚舉右端點
            # 保存以 x 為右端點的所有 OR 結果，注意由於 OR 的性質，這裡的 st2 在迴圈結束後是遞增的
            st2 = [x]
            for y in st:
                # 保持有序性質以便去重，省去一個 set
                if y | x != st2[-1]:
                    st2.append(y | x)
            # assert all(a < b for a, b in pairwise(st2))
            st = st2
            ans.update(st)
        return len(ans)
    
class Solution1c:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        # 枚舉右端點 i，在枚舉 i 時將 nums[j] 原地修改成 OR(nums[j...i])
        # 此時有 A_j ⊇ A_{j+1} ⊇ A_{j+2} ⊇ ... ⊇ A_i 的性質，即 A_{j+1} 是 A_j 的子集，以此類推
        for i, x in enumerate(arr):
            ans.add(x)
            for j in range(i - 1, -1, -1):
                # 如果 x 是 nums[j] 的子集，則 x 也會是 nums[j-1] 的子集，以此類推，故不用更新
                if arr[j] | x == arr[j]:
                    break
                arr[j] |= x
                ans.add(arr[j])
        return len(ans)
    
# Solution = Solution1a
Solution = Solution1b
# Solution = Solution1c
# @lc code=end

