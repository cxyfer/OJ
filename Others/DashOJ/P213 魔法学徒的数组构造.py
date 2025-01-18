n = int(input())
A = list(map(int, input().split()))
B = [0] * n

vis = set()
for i, x in enumerate(A, 1):
    tgt = i - (x % i)
    while tgt in vis:
        tgt += i
    vis.add(tgt)
    B[i - 1] = tgt

print(*B)