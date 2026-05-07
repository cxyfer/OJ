from heapq import heappush, heappop
from collections import defaultdict


def solve1():
    buildings = []
    while True:
        try:
            l, h, r = map(int, input().split())
            buildings.append((l, h, r))
        except EOFError:  # 輸入結束
            break
        except ValueError:  # 輸入不足 3 個數
            break

    W = max(r for _, _, r in buildings)

    skyline = [0] * (W + 1)
    for l, h, r in buildings:
        for i in range(l, r):
            skyline[i] = max(skyline[i], h)

    ans = []
    prev_h = 0
    for i, h in enumerate(skyline):
        if h != prev_h:
            ans.append(f"{i} {h}")
            prev_h = h
    print(*ans)


def solve2():
    buildings = []
    while True:
        try:
            l, h, r = map(int, input().split())
            buildings.append((l, h, r))
        except EOFError:  # 輸入結束
            break
        except ValueError:  # 輸入不足 3 個數
            break

    Xs = set()
    events = defaultdict(list)
    for l, h, r in buildings:
        events[l].append((h, r))
        Xs.add(l)
        Xs.add(r)

    ans = []
    prev_h = 0
    hp = []
    for l in sorted(Xs):
        for h, r in events[l]:
            heappush(hp, (-h, r))

        while hp and hp[0][1] <= l:
            heappop(hp)

        h = -hp[0][0] if hp else 0
        if h != prev_h:
            ans.append(f"{l} {h}")
            prev_h = h
    print(*ans)


# solve = solve1
solve = solve2

if __name__ == "__main__":
    solve()
