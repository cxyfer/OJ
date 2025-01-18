s = input()
ans = "/"
i = 1
for ch in s:
    if ch == ']':
        break
    if ch.isupper():
        ans += ch.lower()
print(ans)