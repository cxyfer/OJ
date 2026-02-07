"""
A. 宙天
https://ac.nowcoder.com/acm/contest/120563/A
簽到

由於 k^2 < k(k+1) = n < (k+1)^2，所以 k < sqrt(n) < k+1。
因此 k 只可能是 int(sqrt(n)) ，判斷 k * (k + 1) 是否等於 n 即可。
"""
from math import sqrt

def solve():
    x = int(input())
    
    k = int(sqrt(x))
    print("YES" if k * (k + 1) == x else "NO")

if __name__ == "__main__":
    solve()