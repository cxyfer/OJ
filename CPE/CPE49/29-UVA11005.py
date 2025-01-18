"""
    UVA 的測資能過，但是 CPE 的測資格式和題目敘述不同，所以要改讀取方式
"""

buffer = []

def cin():
    global buffer
    if len(buffer) == 0:
        buffer = input().split()
    res = buffer[0]
    buffer = buffer[1:]
    return res

T = int(cin())

for tc in range(1, T+1):
    costs = [int(cin()) for _ in range(36)]
    k = int(cin())
    if tc > 1:
        print()
    print(f"Case {tc}:")
    for _ in range(k):
        n = int(cin())
        min_r, min_s = [], float("inf")
        for r in range(2, 37):
            nn = n
            s = 0
            while nn:
                s += costs[nn % r]
                nn //= r
            if s < min_s:
                min_r, min_s = [r], s
            elif s == min_s:
                min_r.append(r)
        print(f"Cheapest base(s) for number {n}: {' '.join(map(str, min_r))}")