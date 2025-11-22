"""
本題是 Easy 版本，只需考慮值為 0/1 的情況。

顯然只有在某一個位置上 A 和 B 的值不同時，操作這個位置才有意義。
此外，如果 A 和 B 的奇偶性相同，那麼無論怎麼操作，都不可能使 A 和 B 的奇偶性不同。
因此在存在影響結果的位置時，判斷最後一個位置能由誰操作。
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    pos = [i for i in range(n) if A[i] != B[i]]

    if len(pos) == 0 or (sum(A) & 1) == (sum(B) & 1):
        print("Tie")
    else:
        if pos[-1] & 1 == 0:
            print("Ajisai")
        else:
            print("Mai")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()