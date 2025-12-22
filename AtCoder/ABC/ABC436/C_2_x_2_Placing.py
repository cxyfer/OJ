def solve():
    N, M = map(int, input().split())
    vis = set()
    for _ in range(M):
        r, c = map(int, input().split())
        if any((x, y) in vis for x in range(r, r + 2) for y in range(c, c + 2)):
            continue
        for x in range(r, r + 2):
            for y in range(c, c + 2):
                vis.add((x, y))
    print(len(vis) // 4)

if __name__ == "__main__":
    solve()