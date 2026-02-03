"""
C. Array Covering
https://ac.nowcoder.com/acm/contest/120561/C

注意到我們總是可以將除了兩端的數字變成 max(A)
- 當 max(A) 在兩側時，顯然可以選取 (0, n-1)
- 當 max(A) 在中間時，同樣可以分兩次操作 (0, i) 和 (i, n-1)
因此答案為 max(A) * (n - 2) + A[0] + A[-1]
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))

    ans = A[0] + A[-1] + (n - 2) * max(A)
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()