"""
A. A+B Problem
https://ac.nowcoder.com/acm/contest/120561/A
枚舉 + 概率計算
"""
MOD = 998244353
inv100 = pow(100, MOD - 2, MOD)

# 0~9 的七段顯示器顯示方式
PATTERNS = {
    0: (1, 1, 1, 0, 1, 1, 1),
    1: (0, 0, 1, 0, 0, 1, 0),
    2: (1, 0, 1, 1, 1, 0, 1),
    3: (1, 0, 1, 1, 0, 1, 1),
    4: (0, 1, 1, 1, 0, 1, 0),
    5: (1, 1, 0, 1, 0, 1, 1),
    6: (1, 1, 0, 1, 1, 1, 1),
    7: (1, 0, 1, 0, 0, 1, 0),
    8: (1, 1, 1, 1, 1, 1, 1),
    9: (1, 1, 1, 1, 0, 1, 1),
}

def solve():
    C = int(input())
    P = list(map(int, input().split()))
    
    probs = [-1] * 10
    for d, pattern in PATTERNS.items():
        prob = 1
        for p, c in zip(P, pattern):
            if c == 1:
                prob = (prob * (p * inv100)) % MOD
            else:
                prob = (prob * (1 - (p * inv100))) % MOD
        probs[d] = prob
    
    ans = 0
    for A in range(C + 1):
        B = C - A
        cur = 1
        for _ in range(4):
            cur = (cur * probs[A % 10]) % MOD
            A //= 10
            cur = (cur * probs[B % 10]) % MOD
            B //= 10
        ans = (ans + cur) % MOD
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()