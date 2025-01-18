"""
    BFS
    總是跳到下一個屬於不同按鍵的單元方塊的方式
    有點類似 SPFA (Shortest Path Faster Algorithm)

    看到 30s 的時間限制就知道不是給 Python 寫的，乖乖用 C++ 吧。
    CPE 測試能通過，但是 UVA 會 TLE
"""
from collections import deque

import sys
def input(): return sys.stdin.readline().strip()
def print(val=""): sys.stdout.write(str(val) + '\n')

def to_int(s: str) -> int:
    if s.isdigit():
        return int(s)
    elif s.isalpha():
        return ord(s) - ord('A') + 10
    elif s == '-':
        return 36
    else: # s == '*', enter
        return 37
    
while True:
    try:
        r, c = map(int, input().split())
    except:
        break
    kb = [[to_int(ch) for ch in input()] for _ in range(r)]
    s = [to_int(ch) for ch in input()] + [37] # 最後需要 Enter 鍵
    # 預處理下一個與當前按鍵不同的按鍵
    nxt = [[[] for j in range(c)] for i in range(r)]
    for x in range(r):
        for y in range(c):
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                while 0 <= nx < r and 0 <= ny < c and kb[nx][ny] == kb[x][y]:
                    nx, ny = nx + dx, ny + dy
                if 0 <= nx < r and 0 <= ny < c:
                    nxt[x][y].append((nx, ny))
    # BFS
    ans = float("inf")
    q = deque([(0, 0, 0, 0)])
    visited = [[-1] * c for _ in range(r)] # 走到 (x, y) 時，已經找到的字元數是多少
    while q:
        x, y, idx, step = q.popleft()
        if kb[x][y] == s[idx]: # 當前按鍵與目標字元相同
            if idx == len(s) - 1: # 找到答案
                ans = step + 1
                break
            q.append((x, y, idx+1, step+1)) # 按下當前按鍵，找下一個字元
            visited[x][y] = max(visited[x][y], idx+1)
        else:
            for nx, ny in nxt[x][y]:
                if visited[nx][ny] >= idx: # 剪枝，到達 (nx, ny) 時已經找到的字元數比當前多
                    continue
                visited[nx][ny] = idx
                q.append((nx, ny, idx, step+1)) # 移動到 (nx, ny)
    print(ans)