s = input()
n = len(s)

cnt = [0] * 26
for ch in s:
    cnt[ord(ch) - ord('A')] += 1

if max(cnt) > (n + 1) // 2:
    exit(print(-1))

ans = []
last = -1
for pos in range(n):
    mx1 = mx2 = 0
    mx_id = -1
    for i in range(26):
        if cnt[i] > mx1:
            mx1, mx2 = cnt[i], mx1
            mx1_id = i
        elif cnt[i] > mx2:
            mx2 = cnt[i]

    rem = n - pos - 1
    limit = (rem + 1) // 2
    for c in range(26):
        if c == last or cnt[c] == 0:
            continue
        n_mx = mx1 if c != mx1_id else max(mx2, cnt[c] - 1)
        if n_mx <= limit:
            cnt[c] -= 1
            ans.append(chr(ord('A') + c))
            last = c
            break
    else:
        exit(print(-1))

print("".join(ans))