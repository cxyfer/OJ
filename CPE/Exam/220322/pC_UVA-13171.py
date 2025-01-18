""" UVA-13171: Pixel Art
    模擬(Simulation)
    已於 UVA, CPE, ZeroJudge 測試通過
"""
t = int(input())

for _ in range(t):
    m, y, c, s = input().split()
    m, y, c = map(int, [m, y, c]) # magenta, yellow, cyan
    flag = True
    for ch in s:
        if ch == 'M':
            m -= 1
        elif ch == 'Y':
            y -= 1
        elif ch == 'C':
            c -= 1
        elif ch == 'R':
            m -= 1
            y -= 1
        elif ch == 'V':
            m -= 1
            c -= 1
        elif ch == 'G':
            y -= 1
            c -= 1
        elif ch == 'B':
            m -= 1
            y -= 1
            c -= 1
        if m < 0 or y < 0 or c < 0:
            flag = False
            break
    print(f"YES {m} {y} {c}" if flag else 'NO')