"""
    AC: UVA, CPE, ZeroJudge
"""
t = int(input())

for kase in range(1, t+1):
    sites = []
    mx = 0
    for _ in range(10):
        url, v = input().split()
        v = int(v)
        sites.append((url, v))
        mx = max(mx, v)
    print(f"Case #{kase}:")
    for url, v in sites:
        if v == mx:
            print(url)