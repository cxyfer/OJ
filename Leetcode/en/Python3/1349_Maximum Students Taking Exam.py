# @algorithm @lc id=1471 lang=python3 
# @title maximum-students-taking-exam


from en.Python3.mod.preImport import *
# @test([["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]])=4
# @test([[".","#"],["#","#"],["#","."],["#","#"],[".","#"]])=3
# @test([["#",".",".",".","#"],[".","#",".","#","."],[".",".","#",".","."],[".","#",".","#","."],["#",".",".",".","#"]])=10
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        arr = [0] * m # arr[i] 是第 i 排的狀態，即可用椅子的下標集合(二進位)，0 表示可以坐，1 表示不能坐 
        for i, row in enumerate(seats):
            for j, ch in enumerate(row):
                if ch == '.':
                    arr[i] |= 1 << j
        # dfs(i, j) 表示第 i 排坐滿 j 這種狀態的最大人數，總共有 2^n 種狀態
        @cache # Memoization
        def dfs(i: int, j: int) -> int:
            if i == 0:
                lb = j & -j # low bit 最低位的 1，貪心思路，先坐最左邊(最低位)的人
                return dfs(i, j & ~(lb * 3)) + 1 if j else 0 # 由將 lb 和 lb 左邊的位置都設為 0 的狀態轉移，即 j & ~(lb | lb << 1) = j & ~(lb * 3)
            res = dfs(i - 1, arr[i - 1])  # 第 i 排不坐人
            s = j
            while s: # 枚舉 j 的子集 s，即當前這排的可能狀態
                if (s & (s >> 1)) == 0: # 左右相鄰的位置都沒有人，即 沒有連續兩個 1
                    t = arr[i - 1] & ~(s << 1 | s >> 1) # 當前狀態下，前一排可以坐的位置，即當前這排為1的位置的左右兩邊，在前一排都不坐人
                    res = max(res, dfs(i - 1, t) + s.bit_count()) # 狀態轉移，即前一排坐滿 t 這種狀態的最大人數 + 當前這排坐滿 s 這種狀態的人數
                s = (s - 1) & j # 考慮下一個子集
            return res
        return dfs(m-1, arr[-1]) # 第 m-1 排坐滿 arr[-1] 這種狀態的最大人數