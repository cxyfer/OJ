from collections import deque

COLORS = "rgb"

def solve(player):
    if player == "first":
        n, m = map(int, input().split())

        g = [[] for _ in range(n)]
        for _ in range(m):
            u, v = map(lambda x: int(x) - 1, input().split())
            g[u].append(v)
            g[v].append(u)
        
        color = [''] * n
        vis = [False] * n
        vis[0] = True
        q = deque([(0, 0)])  # (u, d)
        while q:
            u, d = q.popleft()
            color[u] = COLORS[d % 3]
            for v in g[u]:
                if not vis[v]:
                    vis[v] = True
                    q.append((v, d + 1))
        print("".join(color))
    else:
        q = int(input())
        for _ in range(q):
            d = int(input())
            s = input()
            assert len(s) == d

            colors = sorted(set(s))
            if len(colors) == 1:
                c = colors[0]
            elif len(colors) == 2:
                if 'g' in colors and 'b' in colors:
                    c = 'b'
                elif 'r' in colors and 'b' in colors:
                    c = 'r'
                elif 'r' in colors and 'g' in colors:
                    c = 'g'
            print(s.find(c) + 1)

if __name__ == "__main__":
    player = input()
    t = int(input())
    for _ in range(t):
        solve(player)