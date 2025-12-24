def solve():
    n, q = map(int, input().split())

    B = n.bit_length()
    diff1 = [[0] * (n + 1) for _ in range(B)]
    diff2 = [[0] * (n + 1) for _ in range(B)]

    for _ in range(q):
        l, r = map(int, input().split())
        for b in range(B):
            # 區間內有多少個數是 2^b 的倍數
            # l + k * 2^b - 1 <= r => k <= (r - l + 1) / 2^b
            k = (r - l + 1) >> b
            if k == 0: break
            
            # i − l + 1 = 2^b => i = l + 2^b - 1
            st = l + (1 << b) - 1
            # l + (k+1) * 2^b - 1 > r
            ed = l + ((k + 1) << b) - 1

            diff1[b][st] += 1
            diff2[b][st] += (l - 1)
            if ed <= n:
                diff1[b][ed] -= 1
                diff2[b][ed] -= (l - 1)

    ans = [0] * n
    for b in range(B):
        d = 1 << b
        w = 1 if b == 0 else (1 << (b - 1))
        for i in range(1, n + 1):
            if i >= d:
                diff1[b][i] += diff1[b][i - d]
                diff2[b][i] += diff2[b][i - d]
            ans[i - 1] += (diff1[b][i] * i - diff2[b][i]) * w
    print(*ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()