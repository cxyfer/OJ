from heapq import heappush, heappop

def solve():
    N, K = map(int, input().split())
    customers = [list(map(int, input().split())) for _ in range(N)]

    ans = [-1] * N
    tot = t = 0
    hp = []
    for i, (a, b, c) in enumerate(customers):
        a = max(a, t)
        while tot + c > K:
            ed, cj = heappop(hp)
            tot -= cj
            a = max(a, ed)
        heappush(hp, (a + b, c))
        tot += c
        ans[i] = a
        t = a
    print(*ans, sep='\n')

if __name__ == "__main__":
    solve()