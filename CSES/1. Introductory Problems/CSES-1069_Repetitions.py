s = input()
ans = cur = 1
for i, ch in enumerate(s):
    if i > 0 and ch == s[i-1]:
        cur += 1
    else:
        ans = max(ans, cur)
        cur = 1
ans = max(ans, cur)
print(ans)