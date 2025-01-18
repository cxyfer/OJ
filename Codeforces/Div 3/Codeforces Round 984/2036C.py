t = int(input())

for _ in range(t):
    s = list(" " + input())

    def check(i):
        if i < 0 or i >= len(s) - 3:
            return False
        return s[i] == "1" and s[i + 1] == "1" and s[i + 2] == "0" and s[i + 3] == "0"
    
    cnt = 0
    for i in range(1, len(s) - 3):
        if check(i):
            cnt += 1

    q = int(input())
    for _ in range(q):
        idx, val = map(int, input().split())
        if int(s[idx]) != val:
            bf = check(idx - 3) + check(idx - 2) + check(idx - 1) + check(idx)
            s[idx] = str(val)
            af = check(idx - 3) + check(idx - 2) + check(idx - 1) + check(idx)
            cnt += af - bf
        print("YES" if cnt > 0 else "NO")