"""
    模擬(Simulation)
    由於要求原座標經過操作後的位置，因此可以讓原本的表格中保存原座標的位置，
    這樣在經過表格操作後，只要遍歷表格，就能找出原座標的新位置。

    要用 Python AC 需要一點運氣，同樣的程式碼 從 1.660 到 3.000 TLE
"""
import sys
def input(): return sys.stdin.readline().strip()
def print(val=""): sys.stdout.write(str(val) + '\n')

class Sheet():
    def __init__(self, r, c) -> None:
        self.r = r
        self.c = c
        self.tbl = [[(i+1, j+1) for j in range(c) ] for i in range(r)] # 1-based, original position
    def DR(self, target):
        for i in target:
            self.tbl.pop(i)
        self.r -= len(target)
    def DC(self, target):
        for row in self.tbl:
            for j in target:
                row.pop(j)
        self.c -= len(target)
    def IR(self, target):
        for i in target:
            self.tbl.insert(i, [(0, 0) for _ in range(self.c)])
        self.r += len(target)
    def IC(self, target):
        for row in self.tbl:
            for j in target:
                row.insert(j, (0, 0))
        self.c += len(target)
    def EX(self, pos):
        r1, c1, r2, c2 = pos
        self.tbl[r1][c1], self.tbl[r2][c2] = self.tbl[r2][c2], self.tbl[r1][c1]
    def query(self, x, y):
        for i in range(self.r):
            for j in range(self.c):
                if self.tbl[i][j] == (x, y):
                    return (i+1, j+1)
        return (0, 0)

kase = 1
while True:
    r, c = map(int, input().split())
    if r == 0 and c == 0:
        break
    sheet = Sheet(r, c)
    n = int(input()) # number of operations
    for _ in range(n):
        cmd, *args = input().split()
        args = list(map(lambda x: int(x)-1, args))
        if cmd != "EX": # sort in descending order
            args = sorted(args[1:], reverse=True) 

        if cmd == "DR":
            sheet.DR(args)
        elif cmd == "DC":
            sheet.DC(args)
        elif cmd == "IR":
            sheet.IR(args)
        elif cmd == "IC":
            sheet.IC(args)
        elif cmd == "EX":
            sheet.EX(args)
    
    if kase > 1: print()
    print(f"Spreadsheet #{kase}")
    kase += 1
    m = int(input()) # number of queries
    for _ in range(m):
        x, y = map(int, input().split())
        i, j = sheet.query(x, y)
        if i and j:
            print(f"Cell data in ({x},{y}) moved to ({i},{j})")
        else:
            print(f"Cell data in ({x},{y}) GONE")