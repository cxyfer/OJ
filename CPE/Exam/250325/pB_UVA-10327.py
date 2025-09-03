"""
UVA-10327 Flip Sort
https://vjudge.net/problem/UVA-10327
僅透過交換相鄰元素來排序的次數為逆序對數量，可以用 Bubble Sort 的原理理解。
由於 N <= 1000，可以直接暴力法求解，時間複雜度為 O(N^2)。

進階作法是在 Merge Sort 的過程中維護逆序對數量，或使用 BIT 維護，時間複雜度為 O(N log N)。
注意雖然樣例都是 1~N 的排列，但題目沒有保證，因此用 BIT 的話需要先離散化。
"""
import sys
it = iter(sys.stdin.read().split())
input = lambda: next(it)

while True:
    try:
        N = int(input())
        # A = list(map(int, input().strip().split()))
        A = [int(input()) for _ in range(N)]
    except (EOFError, ValueError, StopIteration):
        break

    # ans = 0
    # for i, x in enumerate(A):
    #     for j in range(i + 1, N):
    #         if x > A[j]:
    #             ans += 1

    # 離散化
    mp = {x: i + 1 for i, x in enumerate(sorted(set(A)))}
    A = [mp[x] for x in A]

    # BIT
    tree = [0] * (N + 2)
    def update(k: int, x: int): # 令 nums[k] += x
        while k < len(tree):
            tree[k] += x
            k += (k & -k)

    def query(k: int) -> int: # 返回 sum(nums[:k+1])
        res = 0
        while k > 0:
            res += tree[k]
            k -= (k & -k)
        return res
    
    ans = 0
    for i, x in enumerate(A):
        ans += i - query(x)
        update(x, 1)

    print(f"Minimum exchange operations : {ans}")