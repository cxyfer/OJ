"""
CF2183A Binary Array Game
https://codeforces.com/contest/2183/problem/A

只要操作後的陣列有 0 ，則 Bob 必勝。
考慮 Alice 在甚麼情況下操作後還會有 0。
- 若原陣列沒有 0，則 Alice 可以直接獲勝
- 若原陣列有 0，Alice 先手不能操作整個陣列，因為這樣會讓 Bob 獲勝
  - 若 A[1] = 0 且 A[n] = 1，則可以操作 [1, n - 1] 構造出 [1, 1]，Bob 必敗。
  - 若 A[1] = 1 且 A[n] = 0，則可以操作 [2, n] 構造出 [1, 1]，同理。
- 只有在 A[1] = 0 且 A[n] = 0 時，Alice 不能操作整個陣列，又不能把 0 消除，故 Bob 獲勝
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    if A[0] == 0 and A[-1] == 0:
        print("Bob")
    else:
        print("Alice")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()