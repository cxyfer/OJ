p1, p2, p3 = map(int, input().split())
s = input()

n = len(s)
ans = ""

for i, ch in enumerate(s):
    pre = ans[-1] if i > 0 else "#"
    suf = s[i + 1] if i + 1 < n else "#"
    if ch == '-' and pre < suf and (pre.islower() and suf.islower() or pre.isdigit() and suf.isdigit()):
        tmp = ""
        if p1 == 1:
            for k in range(ord(pre) + 1, ord(suf)):
                tmp += chr(k) * p2
        elif p1 == 2:
            for k in range(ord(pre) + 1, ord(suf)):
                tmp += chr(k).upper() * p2
        else:
            tmp += '*' * (ord(suf) - ord(pre) - 1) * p2
        if p3 == 1:
            ans += tmp
        else:
            ans += tmp[::-1]
    else:
        ans += ch
print(ans)