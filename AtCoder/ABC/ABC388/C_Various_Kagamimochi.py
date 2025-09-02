"""
Two Pointers
枚舉右維護左，枚舉右端點，維護能疊在右端點上的左端點數量。
時間複雜度為 O(N)
"""

N = int(input())
A = list(map(int, input().split()))

ans = left = 0
for right, a in enumerate(A):
    while A[left] * 2 <= a:
        left += 1
    ans += left
print(ans)