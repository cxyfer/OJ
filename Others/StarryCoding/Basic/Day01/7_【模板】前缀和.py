t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    s = [0]
    for x in A:
        s.append(s[-1] + x)
    for _ in range(q):
        l, r = map(int, input().split())
        print(s[r] - s[l-1])