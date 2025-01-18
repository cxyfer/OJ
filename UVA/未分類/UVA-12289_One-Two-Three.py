t = int(input())

for _ in range(t):
    s = input().strip()
    if len(s) == 5:
        print(3)
    else:
        diff_1 = sum(1 for i in range(3) if s[i] != "one"[i])
        print(1 if diff_1 == 1 else 2)