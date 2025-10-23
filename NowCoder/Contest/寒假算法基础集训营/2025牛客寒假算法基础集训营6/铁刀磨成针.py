"""
J - 铁刀磨成针
https://ac.nowcoder.com/acm/contest/95338/J
 
貪心 + 枚舉
不難發現最優的策略是先磨刀，然後一邊磨刀一邊攻擊，最後再不磨刀只攻擊
   ____
  /    \
 /      \
/

枚舉只磨刀不攻擊的次數 a，則：
- 磨刀後攻擊的次數 b = min(y - a, n - a)
- 不磨刀只攻擊的次數 c = min(n - a - b, x + a)

注意磨刀後再攻擊會先使攻擊力 +1。
"""

def solve():
    n, x, y = map(int, input().split())

    ans = 0
    for a in range(min(n, y) + 1):  # 枚舉只磨刀不攻擊的次數 a
        b = min(y - a, n - a)  # 磨刀後攻擊的次數 b，攻擊力為 x + a + 1
        c = min(n - a - b, x + a)  # 不磨刀只攻擊的次數 c，攻擊力為 x + a, x + a - 1, ..., x + a - c + 1
        ans = max(ans, (x + a + 1) * b + (x + a + x + a - c + 1) * c // 2)
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()