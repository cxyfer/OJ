"""
    貪心，逐位計算最大的結果
"""

N, Q = map(int, input().split())
A = list(map(int, input().split()))
K = [int(input()) for _ in range(Q)]

for k in K:
    B = A.copy() # 複製一份
    for b in range(60, -1, -1): # 逐位計算
        s = 0
        for i in range(N):
            if B[i] & (1 << b):
                s += (1 << b) - B[i] # 計算差值
            
