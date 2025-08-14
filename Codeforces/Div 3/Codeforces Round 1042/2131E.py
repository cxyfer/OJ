"""
由於每個位置 i 只能操作一次，考慮 i 和 i + 1 的操作順序，
若先操作 i，則此時 A[i + 1] 尚未被操作過，因此 A[i] <- A[i] ^ A[i + 1]；
同理若先操作 i + 1，則此時操作後的 A[i + 1] 必為 B[i + 1]，因此 A[i] <- A[i] ^ B[i + 1]。
"""
t = int(input())

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if A[-1] != B[-1]:
        print("NO")
        return
    
    for i in range(n - 2, -1, -1):
        if A[i] != B[i] \
            and (A[i] ^ A[i + 1]) != B[i] \
            and (A[i] ^ B[i + 1]) != B[i]:
            print("NO")
            break
    else:
        print("YES")

for _ in range(t):
    solve()