N, X, Y = map(int, input().split())
As = list(map(int, input().split()))

x, y = 0, 0
ans = [0 for _ in range(N)]
dir_idx = 1
DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def solve(i, dir_idx, x, y): # backtracking
    if i == N:
        if x == X and y == Y:
            print("Yes")
            print("".join(ans))
            return True
        return False
    for turn in [-1, 1]: # LR
        ans[i] = "L" if turn == -1 else "R"
        # dir
        dx, dy = DIRS[(dir_idx + turn) % 4]
        # print(i, x, y, dx, dy)
        if solve(i+1, dir_idx + turn, x + dx * As[i], y + dy * As[i]):
            return True
    return False

res = solve(0, dir_idx, 0, 0)
if not res:
    print("No")
