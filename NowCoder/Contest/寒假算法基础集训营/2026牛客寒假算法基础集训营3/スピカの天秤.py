"""
G. スピカの天秤
https://ac.nowcoder.com/acm/contest/120563/G

當兩側重量相等時，移除任一側的任一個元素皆可破壞平衡，答案為 1。
否則，我們可以貪心地從較重的那一側中移除最大值，直到大小關係被打破。
"""
def solve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    assert len(A) == n and len(B) == m

    s1, s2 = sum(A), sum(B)

    if s1 == s2:
        print(1)
    else:
        if s1 < s2:
            A, B = B, A
            s1, s2 = s2, s1
        A.sort(reverse=True)
        i = 0
        while s1 > s2:
            s1 -= A[i]
            i += 1
        print(i)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()