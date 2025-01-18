# @algorithm @lc id=1539 lang=python3 
# @title diagonal-traverse-ii


from en.Python3.mod.preImport import *
# @test([[1,2,3],[4,5,6],[7,8,9]])=[1,4,2,7,5,3,8,6,9]
# @test([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]])=[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
class Solution:
    """
        對於 matrix[i][j]，其對角線編號為 i+j
    """
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        lst = defaultdict(list)
        for i, row in enumerate(nums):
            for j, v in enumerate(row):
                lst[i+j].append(v)
        ans = []
        for k in sorted(lst.keys()):
            ans += lst[k][::-1] # 逆序
        return ans