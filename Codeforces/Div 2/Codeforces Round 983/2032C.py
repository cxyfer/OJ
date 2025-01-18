"""
排序後，只需要確保最小的兩個數 A[0] + A[1] <= A[r], 2 <= r < n 即可。

但是當 A[0] + A[1] > A[r] 時，則不滿足要求，此時需要調整，
這裡的思考方式是將 A[0] 改成 A[n - 1]，這樣一定會在後續過程中被考慮到
但在修改後，最小的兩個數變成 A[1] 和 A[2]，因此我們需要使用 l 維護當前最小的兩個數

最後答案就是 l 移動的次數
"""

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()

    ans = 0
    l = 0
    for r in range(2, n):
        if A[l] + A[l + 1] <= A[r]:
            l += 1
    print(l)