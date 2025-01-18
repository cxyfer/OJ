T = int(input())

for _ in range(T):
    s, d = map(int, input().split())
    a = (s + d) / 2
    b = s - a
    if a >= 0 and b >= 0 and a == int(a) and b == int(b):
        print(int(a), int(b))
    else:
        print("impossible")