"""
C. 小苯的数字合并
https://ac.nowcoder.com/acm/contest/116658/C

注意 ai >= 1，因此對不同位置合併產生的結果一定是不同的，
故考慮每個相鄰的位置是否合併即可。
"""
MOD = 998244353

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n
    print(pow(2, n - 1, MOD))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()