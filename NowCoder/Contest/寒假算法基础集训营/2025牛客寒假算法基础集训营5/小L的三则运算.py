"""
A - 小L的三则运算
https://ac.nowcoder.com/acm/contest/95337/A
"""
def solve():
    n, op = input().split()
    n = int(n)
    if op == '+':
        print(1, n - 1)
    elif op == '-':
        print(n + 1, 1)
    elif op == '*':
        print(1, n)

if __name__ == "__main__":
    solve()