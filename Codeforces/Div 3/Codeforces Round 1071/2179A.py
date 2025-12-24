def solve():
    k, x = map(int, input().split())
    print(k * x + 1)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()