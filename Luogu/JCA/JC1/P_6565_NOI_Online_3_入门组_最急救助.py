n = int(input())

mx = 0
ans = []
for _ in range(n):
    name = input()
    s = input()
    cnt = 0
    for i in range(len(s) - 2):
        if s[i] == 's' and s[i + 1] == 'o' and s[i + 2] == 's':
            cnt += 1
    if cnt > mx:
        mx = cnt
        ans = [name]
    elif cnt == mx:
        ans.append(name)

print(*ans)
print(mx)
