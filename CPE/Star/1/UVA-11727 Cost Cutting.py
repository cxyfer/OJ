t = int(input())

for kase in range(1, t + 1):
    x, y, z = sorted(map(int, input().split()))
    print(f"Case {kase}: {y}")
