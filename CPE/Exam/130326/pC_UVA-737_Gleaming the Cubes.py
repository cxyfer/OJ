while True:
    n = int(input())
    if n == 0:
        break
    lx = ly = lz = -float('inf')
    rx = ry = rz = float('inf')
    for _ in range(n):
        x, y, z, l = map(int, input().split())
        lx = max(lx, x)
        ly = max(ly, y)
        lz = max(lz, z)
        rx = min(rx, x + l)
        ry = min(ry, y + l)
        rz = min(rz, z + l)
    print(max(0, (rx - lx) * (ry - ly) * (rz - lz)))