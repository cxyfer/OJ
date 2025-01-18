t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if n == 1:
        print("1")
        print("1")
        continue

    if k == 1 or k == n:
        print("-1")
        continue

    # 1. [1, k-1], [k, k], [k+1, n]
    if (k - 1) & 1: # 可以分成三段都是奇數
        print("3")
        print(1, k, k + 1)
    # 2. [1, k-2], [k-1, k+1], [k+2, n]
    else: # 第一段和第三段是偶數，需要調整，各搬動一個第二段即可
        print("3")
        print(1, k - 1, k + 2)