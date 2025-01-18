"""
    Python 會 TLE
"""
import sys
input = sys.stdin.readline
def print(val=""): sys.stdout.write(str(val) + "\n")

t = int(input())

def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def area(p1, p2, p3):
    d1 = dist(p1, p2)
    d2 = dist(p1, p3)
    d3 = dist(p2, p3)
    s = (d1 + d2 + d3) / 2
    return (s * (s - d1) * (s - d2) * (s - d3)) ** 0.5

anses = []
for _ in range(t):
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    def check(a, b, c):
        A = area(points[a], points[b], points[c])
        for i in range(n):
            if (i == a or i == b or i == c): continue
            tmp = area(points[a], points[b], points[i]) + area(points[a], points[c], points[i]) + area(points[b], points[c], points[i])
            if (abs(tmp - A) < 1e-6):
                return False
        return True

    f = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        f[i][i] = 0
    for i in range(n - 1):
        f[i][i + 1] = 0
    for ln in range(3, n + 1): # 枚舉長度
        for i in range(n - ln + 1): # 枚舉左端點
            j = i + ln - 1 # 右端點
            for k in range(i + 1, j): # 枚舉分界點
                if (check(i, k, j)):
                    f[i][j] = min(f[i][j], max(f[i][k], f[k][j], area(points[i], points[k], points[j])))
    # print(f"{f[0][n - 1]:.1f}")
    anses.append(f"{f[0][n - 1]:.1f}")

print("\n".join(anses))