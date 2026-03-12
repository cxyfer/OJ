def solve():
    N, D, K = map(int, input().split())
    W = list(map(int, input().split()))
    print(sum(w - D * K > 0 for w in W))


if __name__ == "__main__":
    solve()
