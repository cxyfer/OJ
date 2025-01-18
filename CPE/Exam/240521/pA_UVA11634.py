"""
    Maybe TLE on UVA, need to optimize I/O and try again.
    多試幾次，有時候會過

    AC: UVA, CPE, ZeroJudge
"""
import sys
input = sys.stdin.readline
def print(val=""):
    sys.stdout.write(str(val) + "\n")

while True:
    n = int(input())
    if n == 0:
        break
    ans = 0
    visited = [False] * 10000
    while not visited[n]:
        ans += 1
        visited[n] = True
        n = (n * n) // 100 % 10000
    print(ans)