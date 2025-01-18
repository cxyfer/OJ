def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def dist2(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

class City:
    def __init__(self, data: list[int]):
        x1, y1, x2, y2, x3, y3, price = data
        self.points = [(x1, y1), (x2, y2), (x3, y3), self.get_last_point(x1, y1, x2, y2, x3, y3)]
        self.price = price
    
    @staticmethod
    def get_last_point(x1, y1, x2, y2, x3, y3):
        ab, ac, bc = dist2(x1, y1, x2, y2), dist2(x1, y1, x3, y3), dist2(x2, y2, x3, y3)
        if ab == ac + bc:
            return x1 + x2 - x3, y1 + y2 - y3
        elif ac == ab + bc:
            return x1 + x3 - x2, y1 + y3 - y2
        elif bc == ab + ac:
            return x2 + x3 - x1, y2 + y3 - y1

t = int(input())

for _ in range(t):
    n, price, A, B = map(int, input().split())
    citys = [City(list(map(int, input().split()))) for _ in range(n)]

    m = n * 4
    g = [[float('inf')] * m for _ in range(m)]

    # 建圖
    for (k, city) in enumerate(citys):  # 城市內
        for i, p1 in enumerate(city.points):
            for j, p2 in enumerate(city.points):
                g[k * 4 + i][k * 4 + j] = dist(p1[0], p1[1], p2[0], p2[1]) * city.price
    for (i, city1) in enumerate(citys): # 城市間
        for (j, city2) in enumerate(citys):
            if i == j:
                continue
            for (k1, p1) in enumerate(city1.points):
                for (k2, p2) in enumerate(city2.points):
                    g[i * 4 + k1][j * 4 + k2] = dist(p1[0], p1[1], p2[0], p2[1]) * price

    # Floyd-Warshall
    for k in range(m):
        for i in range(m):
            if g[i][k] == float('inf'):
                continue
            for j in range(m):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    
    # Answer
    A, B = A - 1, B - 1
    ans = float('inf')
    for i in range(4):
        for j in range(4):
            ans = min(ans, g[A * 4 + i][B * 4 + j])
    print(f'{ans:.1f}')