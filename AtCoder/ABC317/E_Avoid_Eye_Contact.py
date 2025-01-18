# BFS
# 構建迷宮的矩陣，並在上下左右加上牆壁，以免出界
H , W = map(int, input().split(" "))
Maze = [list(f"#{input()}#") for _ in range(H)]
Maze = [["#"]*(W+2)] + Maze + [["#"]*(W+2)]

# 先找出起點、終點、以及所有的箭頭位置
start = goal = None
arrows = []
for i in range(1, H+1):
    for j in range(1, W+1):
        if Maze[i][j] == "S":
            start = (i, j)
        elif Maze[i][j] == "G":
            goal = (i, j)
        elif Maze[i][j] in "<>^v":
            arrows.append((i, j))
# 再來處理箭頭
arrow_map = {"<":(0, -1), ">":(0, 1), "^":(-1, 0), "v":(1, 0)}
for pi, pj in arrows:
    di, dj = arrow_map[Maze[pi][pj]]
    i, j = pi+di, pj+dj
    while Maze[i][j] not in "#<>^v":
        Maze[i][j] = "!" # 為了不影響其他箭頭的判定情況，先標記為"!"
        i, j = i+di, j+dj
# 最後將地圖中的可走路徑標記為0，牆壁或可視為牆壁的符號標記為-1
# 這樣就可以用BFS來走迷宮了，且這個矩陣的元素代表路徑長度
for i in range(H+2):
    for j in range(W+2):
        if Maze[i][j] in "#!<>^v":
            Maze[i][j] = -1
        else:
            Maze[i][j] = 0
# BFS
from collections import deque
queue = deque([start])
while queue:
    pi, pj = queue.popleft()
    if (pi, pj) == goal: # 找到終點就停止
        break
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
        if Maze[pi+di][pj+dj] == 0: #檢查上下左右是否可走且未走過
            Maze[pi+di][pj+dj] = Maze[pi][pj] + 1
            queue.append((pi+di, pj+dj))
print(-1) if Maze[goal[0]][goal[1]] == 0 else print(Maze[goal[0]][goal[1]])


# printMaze()

def printMaze():
    for i in range(1, H+1):
        for j in range(1, W+1):
            print(Maze[i][j], end="")
        print()

