def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    assert n == len(A) == len(B)

    mx = mn = 0
    for a, b in zip(A, B):
        mx, mn = max(mx - a, b - mn), min(mn - a, b - mx)
    print(mx) 

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()