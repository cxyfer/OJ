"""
J. 智乃的幻方
https://ac.nowcoder.com/acm/contest/120565/J
簽到題，按題意模擬即可
"""
def solve():
    grid = [list(map(int, input().split())) for _ in range(3)]

    row = [0] * 3
    col = [0] * 3
    diag = [0] * 2
    vis = set()
    for i in range(3):
        for j in range(3):
            x = grid[i][j]
            vis.add(x)
            row[i] += x
            col[j] += x
            if i == j:
                diag[0] += x
            if i + j == 2:
                diag[1] += x

    if len(vis) == 9 and row[0] == row[1] == row[2] == col[0] == col[1] == col[2] == diag[0] == diag[1]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()