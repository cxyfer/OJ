from bisect import bisect_left

M = 20


def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    pos = [[] for _ in range(M + 1)]
    for i, v in enumerate(A):
        pos[v - 1].append(i)

    # 令 f[s] 表示選擇已經選擇的數字集合為 s 時，最後一個數字的位置
    f = [n] * (1 << M)
    f[0] = -1

    ans = 0
    for s in range(1 << M):
        # 枚舉轉移來源
        t = s
        while t:
            lb = t & -t
            j = lb.bit_length() - 1
            idx = bisect_left(pos[j], f[s ^ lb]) + 1
            if idx < len(pos[j]):
                f[s] = min(f[s], pos[j][idx])
            t ^= lb
        if f[s] < n:
            ans = max(ans, s.bit_count())
    print(ans << 1)


if __name__ == "__main__":
    solve()
