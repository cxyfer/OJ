"""
在 2171C1 的基礎上，將值從 1 增加為 1e6 。
但其實只需要如同 1 位元的情況，找到是否有一個 MSB 能滿足獲勝條件即可。
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for bit in range(20, -1, -1):
        AA = [(a >> bit) & 1 for a in A]
        BB = [(b >> bit) & 1 for b in B]

        pos = [i for i in range(n) if AA[i] != BB[i]]

        if len(pos) == 0 or (sum(AA) & 1) == (sum(BB) & 1):
            continue
        else:
            if pos[-1] & 1 == 0:
                print("Ajisai")
            else:
                print("Mai")
            break
    else:
        print("Tie")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()