def solve():
    n = int(input())
    A = [tuple(map(int, input().split())) for _ in range(n)]
    assert len(A) == n

    s = sum(p for _, p in A)  # 都先去拉雪橇
    A.sort(key=lambda x: x[0] + x[1])

    # 反悔貪心，如果體力還足夠，則讓代價最小的馴鹿坐雪橇
    ans = 0
    for w, p in A:
        s -= (w + p)
        if s < 0:
            break
        ans += 1
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()