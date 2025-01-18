t = int(input())

for _ in range(t):
    s = input()
    ans = int(s)
    for i in range(len(s)):
        ans = min(ans, int(s[i:] + s[:i]))
    print(ans)