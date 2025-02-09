s = input()

n = len(s)
ans = i = 0
while i < n:
    if s[i:i+5] == 'luogu':
        ans += 1
        i += 5
    else:
        i += 1
print(ans)