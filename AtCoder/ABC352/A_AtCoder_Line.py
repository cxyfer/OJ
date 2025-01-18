"""
    題意就是判斷 Z 是否在 X 與 Y 之間
"""
N, X, Y, Z = map(int, input().split())
X, Y = min(X, Y), max(X, Y)
print("Yes" if X <= Z <= Y else "No")