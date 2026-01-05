def solve():
    N = int(input())

    vis = set()
    while N not in vis:
        vis.add(N)
        N = sum(int(digit) ** 2 for digit in str(N))
    print("Yes" if N == 1 else "No")

if __name__ == "__main__":
    solve()