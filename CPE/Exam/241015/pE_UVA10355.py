import math

def dist2(P1, P2):
    return (P1[0] - P2[0]) ** 2 + (P1[1] - P2[1]) ** 2 + (P1[2] - P2[2]) ** 2

while True:
    try:
        name = input()
    except EOFError:
        break
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    P1 = (x1, y1, z1)
    P2 = (x2, y2, z2)
    D = (x2 - x1, y2 - y1, z2 - z1)

    n = int(input())
    spheres = [list(map(int, input().split())) for _ in range(n)]
    intervals = []
    for x, y, z, r in spheres:
        C = (x, y, z)
        E = (P1[0] - C[0], P1[1] - C[1], P1[2] - C[2])

        a = dist2(P1, P2)
        b = 2 * (E[0] * D[0] + E[1] * D[1] + E[2] * D[2])
        c = dist2(P1, C) - r * r

        delta = b * b - 4 * a * c
        if delta <= 0:
            continue
        sqrt_delta = math.sqrt(delta)
        t1 = (-b - sqrt_delta) / (2 * a)
        t2 = (-b + sqrt_delta) / (2 * a)
        t1 = max(0, t1)
        t2 = min(1, t2)
        if t1 <= t2:
            intervals.append((t1, t2))

    # intervals.sort()
    # merged = []
    # for l, r in intervals:
    #     if not merged or l > merged[-1][1]:
    #         merged.append([l, r])
    #     else:
    #         merged[-1][1] = r

    ans = 0
    for l, r in intervals:
        ans += r - l

    print(name)
    print(f"{ans * 100:.2f}")