fact = [1] * 20
for i in range(1, 20):
    fact[i] = fact[i - 1] * i

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    if n == 1:
        print(s)
        continue

    cnt = [0] * 26
    pos = [[] for _ in range(26)]
    for i, ch in enumerate(s):
        cnt[ord(ch) - ord('a')] += 1
        pos[ord(ch) - ord('a')].append(i)

    k1 = fact[n]
    for i, x in enumerate(cnt):
        k1 //= fact[x]
    mx = max(cnt)
    mn = min(v for v in cnt if v > 0)
    k2 = k1 // (mx + 1) * (mn)
    # print(k1, k2)

    if mx == mn:
        idx1 = idx2 = -1
        for ch, ps in enumerate(pos):
            if len(ps) == 0:
                continue
            if idx1 == -1:
                idx1 = ps[0]
            else:
                idx2 = ps[0]
                break
    else:
        idx1 = s.index(chr(ord('a') + cnt.index(mx)))
        idx2 = s.index(chr(ord('a') + cnt.index(mn)))
    lst = list(s)
    lst[idx2] = lst[idx1]
    s = ''.join(lst)
    print(s)