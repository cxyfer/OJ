"""
UVA-10690 Expression Again
https://vjudge.net/problem/UVA-10690
DP

由於 N + M 的數量可以到 110，回溯法會 TLE
注意到 A[i] 的值域很小，可以用 DP 維護可以透過 k 個元素組合出來的和

Python TLE，C++ AC
"""
while True:
    try:
        N, M = map(int, input().split())
        A = list(map(int, input().split()))
    except EOFError:
        break
    except StopIteration:
        break

    tot = sum(A)
    k = min(N, M)
    # f[k] 表示可以透過 k 個元素組合出來的和
    f = [set() for _ in range(k + 1)]
    f[0].add(0)
    for x in A:
        for i in range(k - 1, -1, -1):
            for y in f[i]:
                f[i + 1].add(y + x)
    ans = [float('-inf'), float('inf')]
    for y in f[k]:
        v = y * (tot - y)
        ans[0] = max(ans[0], v)
        ans[1] = min(ans[1], v)
    print(*ans)