from collections import Counter

def solve():
    s, t = input(), input()
    cnt_s, cnt_t = Counter(s), Counter(t)

    cnt_t.subtract(cnt_s)
    if any(cnt_t[c] < 0 for c in cnt_t):
        print("Impossible")
        return

    ans = ""
    last = 0
    for ch in s:
        c = ord(ch) - ord('a')
        if last < c:
            for d in range(last, c):
                d = chr(d + ord('a'))
                ans += d * cnt_t[d]
            last = c
        ans += ch
    for d in range(last, 26):
        d = chr(d + ord('a'))
        ans += d * cnt_t[d]
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()