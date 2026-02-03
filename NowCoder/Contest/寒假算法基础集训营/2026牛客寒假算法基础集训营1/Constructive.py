"""
K. Constructive
https://ac.nowcoder.com/acm/contest/120561/K
簽到題，只有當 n = 1 或 3 時，才有解
"""
def solve():
    n = int(input())
    if n == 1 or n == 3:
        print("YES")
        print(*range(1, n + 1))
    else:
        print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()