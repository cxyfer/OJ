def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert n == len(A)

    st = set(A)
    vis = set()
    ans = []
    for x in sorted(st):  # 從小到大枚舉，保證不重複
        if x in vis:
            continue
        ans.append(x)
        vis.add(x)
        for y in range(2 * x, k + 1, x):
            if y not in st:
                print(-1)
                return
            vis.add(y)
    if len(st) != len(vis):
        print(-1)
        return
    print(len(ans))
    print(*ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()