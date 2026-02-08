"""
H. Tic Tac DREAMIN’
https://ac.nowcoder.com/acm/contest/120563/H

AB = (x2 - x1, y2 - y1)
AO = (x - x1, -y1)
|AB x AO| = 4
|(x2 - x1)(-y1) - (y2 - y1)(x - x1)| = 4
|(y1 - y2)x + (x1y2 - x2y1)| = 4
|ax + b| = 4
"""
def solve():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    a = y1 - y2
    b = x1 * y2 - x2 * y1

    if a == 0:
        if abs(b) == 4:
            print(0)
        else:
            print("no answer")
    else:
        print(f"{(4 - b) / a:.10f}")

if __name__ == "__main__":
    solve()