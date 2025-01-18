t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    words = [input() for _ in range(n)]
    s = 0
    ans = 0
    for word in words:
        if s + len(word) <= m:
            s += len(word)
            ans += 1
        else:
            break
    print(ans)