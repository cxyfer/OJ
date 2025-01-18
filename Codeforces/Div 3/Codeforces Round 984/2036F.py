"""
Reference:
- https://www.bilibili.com/video/BV1RTS6YPEvs/
"""

# 計算 [0, x] 所有數字的 XOR 值
def f(x):
    if x < 0:
        return 0
    r = x % 4
    if r == 0:
        return x
    elif r == 1:
        return 1
    elif r == 2:
        return x + 1
    else:
        return 0

t = int(input())
for _ in range(t):
    l, r, i, k = map(int, input().split())

    # 計算 [l, r] 所有數字的 XOR 值
    A = f(r) ^ f(l - 1)
    
    # 計算 [0, x] 中，所有 mod 2^i = k 的數的 XOR 值
    def g(x):
        if k > x:
            return 0
        if i == 0:
            return f(x)
        # 由於 mod 2^i = k，因此二進位的最後 i 位數一定是 k
        # 可以左移 i 位後思考，會發現情況類似 f(y)
        # 其中 y + 1 是 [0, x] 中，mod 2^i = k 的數字數量
        t = 1 << i
        y = (x - k) // t
        if y < 0:
            return 0
        res = f(y) << i
        if (y + 1) & 1: # 如果是奇數個，要補 k 回來
            res ^= k
        return res
    
    # 計算 [l, r] 中，所有 mod 2^i = k 的數的 XOR 值
    B = g(r) ^ g(l - 1)

    # A XOR B 即為 [l, r] 中，所有 mod 2^i != k 的數的 XOR 值
    print(A ^ B)