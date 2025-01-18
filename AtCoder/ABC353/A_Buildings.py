N = int(input())
H = list(map(int, input().split()))
for i, h in enumerate(H):
    if h > H[0]:
        print(i+1)
        break
else:
    print(-1)