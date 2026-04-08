from heapq import heappush, heappop


def solve():
    n, m = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]

    items.sort(key=lambda x: x[0])

    ans = s = cnt = pre = 0
    hp = []
    for x, t in items:
        s += (x - pre) + t
        heappush(hp, -t)
        cnt += 1
        while hp and s > m:
            s -= -heappop(hp)
            cnt -= 1
        ans = max(ans, cnt)
        pre = x

    print(ans)


if __name__ == "__main__":
    solve()
