from math import ceil, sqrt

while True:
    n = int(input())
    if n == 0:
        break
    m = ceil(sqrt(n))
    no = m * m - n + 1 # 在第 m 層，且是這層的第 no 個 (由大到小)
    if no < m:
        (x, y) = (no, m) if m & 1 else (m, no)
    elif no > m:
        (x, y)= (m, m - (no-m)) if m & 1 else (m - (no-m), m)
    else: # no == m
        x, y = m, m
    print(x, y)
