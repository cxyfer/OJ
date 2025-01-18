run = True
s = ""
while run:
    line = input().strip()
    if not line:
        continue
    if "E" in line: # E 不一定是最後一個字元
        run = False
        line = line[:line.index("E")]
    s += line

for target in [11, 21]:
    x = y = 0
    for ch in s:
        if ch == "W":
            x += 1
        elif ch == "L":
            y += 1
        if max(x, y) >= target and abs(x - y) >= 2:
            print(f"{x}:{y}")
            x = y = 0
    print(f"{x}:{y}")
    print()