"""
J - 小L的汽车行驶问题
https://ac.nowcoder.com/acm/contest/95337/J
"""

def solve():
    n = int(input())
    s = input()
    assert len(s) == n

    ans = cur = 0
    for op in s:
        if op == '0':
            cur += 10
            ans += cur
        elif op == '1':
            cur = max(0, cur - 5)
            ans += cur
        else:
            ans += max(0, cur - 10)
    print(ans)

if __name__ == "__main__":
    solve()