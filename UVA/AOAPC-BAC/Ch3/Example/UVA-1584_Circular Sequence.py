"""
    String
    tags: string, 紫書-Ch3
"""
t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    ans = s
    for i in range(1, n):
        cur = s[i:] + s[:i]
        if cur < ans:
            ans = cur
    print(ans)
