n = int(input())

for _ in range(n):
    l, r = map(int, input().split())
    print(r - l + 1)