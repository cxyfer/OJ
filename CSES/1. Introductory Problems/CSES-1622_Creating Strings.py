s = input()
cnt = [0] * 26
for ch in map(ord, s):
    cnt[ch - ord('a')] += 1

ans = []
path = []
def dfs(i):
    if i == len(s):
        ans.append(''.join(map(chr, path)))
        return
    for j in range(26):
        if cnt[j] > 0:
            cnt[j] -= 1
            path.append(j + ord('a'))
            dfs(i + 1)
            path.pop()
            cnt[j] += 1
dfs(0)
print(len(ans))
print(*ans, sep='\n')