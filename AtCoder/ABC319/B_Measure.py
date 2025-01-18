N = int(input())

ans = ""
for i in range(N+1):
    si = "-"
    for j in range(1, 10):
        if N % j != 0:
            continue
        if i % (N // j) == 0:
            si = str(j)
            break
    ans += si
print(ans)
