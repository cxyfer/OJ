def solve():
    n, m, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    B = (max(A) + m).bit_length()
    ans = 0
    for b in range(B, -1, -1):
        tgt = ans | (1 << b)

        def cost(x):
            if (x & tgt) == tgt:
                return 0
            else:
                msb = (tgt & ~x).bit_length() - 1  # 找出最高缺失位
                y = ((x >> msb) + 1) << msb  # 把最高缺失位變成 1
                y |= tgt & ((1 << msb) - 1)  # 把低位整理成目標值要求的形狀
                return y - x

        if sum(sorted(cost(x) for x in A)[:k]) <= m:
            ans |= 1 << b
    print(ans)


if __name__ == "__main__":
    solve()
