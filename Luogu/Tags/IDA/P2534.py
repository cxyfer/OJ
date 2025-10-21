"""
P2534 [AHOI2012] 铁盘整理
https://www.luogu.com.cn/problem/P2534

IDA* (Iterative Deepening A*)
"""
import sys
sys.setrecursionlimit(2000)

def solve():
    n = int(input())
    A = list(map(int, input().split()))

    # 離散化
    mp = {x: i + 1 for i, x in enumerate(sorted(A))}
    B = [mp[x] for x in A]

    def heuristic(state):
        cnt = 0
        for i in range(n - 1):
            if abs(state[i] - state[i + 1]) != 1:
                cnt += 1
        if state[-1] != n:
            cnt += 1
        return cnt

    def dfs(d, max_d, state) -> bool:
        h = heuristic(state)
        if d + h > max_d:  # Pruning
            return False
        if h == 0:
            return True
        for i in range(1, n):
            next_state = list(state[:i+1][::-1] + state[i+1:])
            if dfs(d + 1, max_d, next_state):
                return True
        return False

    max_d = heuristic(B)
    while max_d <= (n - 1) * 2:
        if dfs(0, max_d, B):
            print(max_d)
            break
        max_d += 1
    else:
        print(-1)

if __name__ == "__main__":
    solve()