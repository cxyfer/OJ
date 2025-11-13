"""
P14357 [CSP-J 2025] 拼数 / number
https://www.luogu.com.cn/problem/P14357
"""
def solve():
    s = input().strip()
    arr = [c for c in s if c.isdigit()]
    arr.sort(reverse=True)
    print(''.join(arr))

if __name__ == "__main__":
    solve()