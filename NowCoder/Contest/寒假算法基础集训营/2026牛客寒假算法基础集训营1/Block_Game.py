"""
E. Block Game
https://ac.nowcoder.com/acm/contest/120561/E

其實就是在 A + [k] 上循環操作，每次將最後面的數字移到最前面，所求為隊首和隊尾的數字和最大值
由於在循環意義下，隊首和隊尾是相鄰的，因此所求是 A + [k] 中循環相鄰元素的最大值
"""
def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    A.append(k)
    ans = A[0] + k
    for a, b in zip(A, A[1:]):
        ans = max(ans, a + b)
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()