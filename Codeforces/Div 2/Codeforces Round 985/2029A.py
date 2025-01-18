t = int(input())

for _ in range(t):
    l, r, k = map(int, input().split())
    ans = r // k - l + 1
    print(max(ans, 0))