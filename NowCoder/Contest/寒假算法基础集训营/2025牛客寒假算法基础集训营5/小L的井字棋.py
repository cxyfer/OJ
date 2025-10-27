"""
E - 小L的井字棋
https://ac.nowcoder.com/acm/contest/95337/E

分類討論
1. 如果場面上沒有棋子
先手可以先下任何一個位置，後手無法堵住所有方向，先手此時使用特權連下兩子可以必勝
2. 如果場面上各有 1 個棋子
同理，此時先手必有一個方向沒有被堵住，可以連下兩子必勝
3. 如果場面上各有 2 個棋子
此時後手也沒有辦法把先手堵死，故還是先手必勝
4. 如果場面上各有 3 個棋子
此時只剩下 C(3, 2) = 3 種情況，枚舉填入後判輸贏即可
5. 如果場面上各有 4 個棋子
此時只剩下 1 種情況，填入後判輸贏即可
"""
from itertools import combinations

def solve():
    grid = [list(input()) for _ in range(3)]

    def check():
        rows = [row.count('X') for row in grid]
        cols = [col.count('X') for col in zip(*grid)]
        diag1 = sum(grid[i][i] == 'X' for i in range(3))
        diag2 = sum(grid[i][2-i] == 'X' for i in range(3))
        return any(row == 3 for row in rows) or any(col == 3 for col in cols) or diag1 == 3 or diag2 == 3

    cnt = sum(row.count('X') for row in grid)
    if cnt <= 2:
        print("Yes")
    elif cnt == 3:
        pos = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 'G']
        for (i1, j1), (i2, j2) in combinations(pos, 2):
            grid[i1][j1] = grid[i2][j2] = 'X'
            if check():
                print("Yes")
                break
            grid[i1][j1] = grid[i2][j2] = 'G'
        else:
            print("No")
    elif cnt == 4:
        i, j = next((i, j) for i in range(3) for j in range(3) if grid[i][j] == 'G')
        grid[i][j] = 'X'
        print("Yes" if check() else "No")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()