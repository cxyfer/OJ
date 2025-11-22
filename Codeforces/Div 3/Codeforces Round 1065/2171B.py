"""
整理得 d = A[n] - A[1]
中間的數字不重要，但為了使字典序最小，中間可以修改的數字應該都修改為 0
- 如果 A[1] 和 A[n] 都能修改，那修改為 0 即可
- 如果 A[1] 和 A[n] 能修改一個，那修改為另一個即可
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))

    for i in range(1, n - 1):
        if A[i] == -1:
            A[i] = 0

    if A[0] == -1 and A[-1] == -1:
        A[0] = A[-1] = 0
    elif A[0] == -1:
        A[0] = A[-1]
    elif A[-1] == -1:
        A[-1] = A[0]

    print(abs(A[-1] - A[0]))
    print(*A)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()