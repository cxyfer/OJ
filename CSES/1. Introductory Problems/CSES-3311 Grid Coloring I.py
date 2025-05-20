n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

# letters = ['A', 'B', 'C', 'D']

# for i, row in enumerate(grid):
#     for j, ch in enumerate(row):
#         for letter in letters:
#             if i > 0 and grid[i - 1][j] == letter \
#                 or j > 0 and grid[i][j - 1] == letter \
#                 or letter == ch:
#                 continue
#             grid[i][j] = letter
#             break

S1 = ['A', 'B']
S2 = ['C', 'D']

for i, row in enumerate(grid):
    for j, v in enumerate(row):
        if (i + j) & 1:
            grid[i][j] = S1[0] if v != S1[0] else S1[1]
        else:
            grid[i][j] = S2[0] if v != S2[0] else S2[1]

for row in grid:
    print(*row, sep='')