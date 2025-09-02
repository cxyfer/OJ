N = int(input())
A = list(map(int, input().split()))

arr = [(x, i) for i, x in enumerate(A)]
arr.sort(reverse=True)

ans = [0] * N
i = 0
r = 1
while i < N:
    st = i
    while i < N and arr[st][0] == arr[i][0]:
        i += 1
    for k in range(st, i):
        ans[arr[k][1]] = r
    r += (i - st)
print('\n'.join(map(str, ans)))
