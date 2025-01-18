# @algorithm @lc id=74 lang=python3 
# @title search-a-2d-matrix


from en.Python3.mod.preImport import *
# @test([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3)=true
# @test([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13)=false
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # return self.solveBy2BinarySearch(matrix, target)
        # return self.solveBy1BinarySearch(matrix, target)
        return self.solveByABST(matrix, target)
    
    """
        1. 2 Binary Search
    """
    def solveBy2BinarySearch(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # 第一次二分搜尋找到target所在的行
        left, right = 0, m-1
        while left <= right: # [left, right]
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        # 第二次二分搜尋找到target所在的列
        row = right
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    """
        2. 1 Binary Search
    """
    def solveBy1BinarySearch(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # 第一次二分搜尋找到target所在的行
        left, right = 0, m*n-1
        while left <= right: # [left, right]
            mid = (left + right) // 2
            x, y = mid // n, mid % n
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    """
        3. Abstract Binary Search Tree
        將二維矩陣抽象成「以右上角為根的 BST」
        1. 若當前節點「大於」目標值，搜索當前節點的「左子樹」，也就是當前矩陣位置的「左方格子」，即 y--
        2. 若當前節點「小於」目標值，搜索當前節點的「右子樹」，也就是當前矩陣位置的「下方格子」，即 x++
        https://leetcode.cn/problems/search-a-2d-matrix/solutions/688573/gong-shui-san-xie-yi-ti-shuang-jie-er-fe-l0pq/
    """
    def solveByABST(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0: # 保證不越界
            if matrix[x][y] > target:
                y -= 1
            elif matrix[x][y] < target:
                x += 1
            else: # matrix[x][y] == target
                return True
        return False
        