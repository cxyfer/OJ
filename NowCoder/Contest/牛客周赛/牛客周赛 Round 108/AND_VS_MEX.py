"""
F. AND VS MEX
https://ac.nowcoder.com/acm/contest/116658/F
SOS DP
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    B = max(A).bit_length()
    U = 1 << B

    # f[s] 表示 s 的超集的 AND 結果
    f = [-1] * U
    for x in A:
        f[x] = x

    for i in range(B):
        s = 0
        while s < U:
            s |= (1 << i)  # 快速跳到 (s >> i) & 1 成立的位置
            f[s ^ (1 << i)] &= f[s]
            s += 1
    
    for s in range(1, U):
        # assert f[s] >= s or f[s] == -1
        if f[s] != s:
            print(s)
            break
    else:
        print(U)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()