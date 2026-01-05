from collections import defaultdict

def solve():
    N = int(input())

    sq = []
    x = 1
    while x * x <= N:
        sq.append(x * x)
        x += 1

    cnt = defaultdict(int)
    for i, x in enumerate(sq):
        for y in sq[i + 1:]:
            if x + y <= N:
                cnt[x + y] += 1
    ans = sorted(x for x, c in cnt.items() if c == 1)
    print(len(ans))
    print(*ans)

if __name__ == "__main__":
    solve()