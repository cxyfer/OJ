def solve():
    N = int(input())
    A = list(map(int, input().split()))

    f0, f1 = 0, abs(A[1] - A[0])
    for i in range(2, N):
        f0, f1 = f1, min(f0 + abs(A[i] - A[i - 2]), f1 + abs(A[i] - A[i - 1]))
    print(f1)

if __name__ == "__main__":
    solve()