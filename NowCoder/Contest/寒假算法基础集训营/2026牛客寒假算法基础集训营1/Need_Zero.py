"""
L. Need Zero
https://ac.nowcoder.com/acm/contest/120561/L
簽到題
"""
def solve():
    n = int(input())
    if n % 10 == 0:
        print(1)
    elif n % 5 == 0:
        print(2)
    elif n % 2 == 0:
        print(5)
    else:
        print(10)

if __name__ == "__main__":
    solve()