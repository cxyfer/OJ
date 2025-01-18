t = int(input())

class Ant:
    def __init__(self, idx=0, pos=0, dir=0):
        self.idx = idx
        self.pos = pos
        self.dir = dir

for kase in range(1, t + 1):
    L, T, N = map(int, input().strip().split())
    bf, af = [], []
    for i in range(N):
        pos, dir = input().strip().split()
        d = 1 if dir == 'R' else -1
        bf.append(Ant(i, int(pos), d))
        af.append(Ant(-1, int(pos) + d * T, d))
    
    bf.sort(key=lambda x: x.pos)
    af.sort(key=lambda x: x.pos)

    for i in range(N - 1):
        if af[i].pos == af[i+1].pos:
            af[i].dir = af[i+1].dir = 2 # 2 means collide

    ans = [Ant() for _ in range(N)]
    for i, (a, b) in enumerate(zip(bf, af)):
        ans[a.idx].pos = b.pos
        ans[a.idx].dir = b.dir
    
    print(f"Case #{kase}:")
    for ant in ans:
        if ant.dir == 2:
            print(ant.pos, 'Turning')
        else:
            if 0 <= ant.pos <= L:
                print(ant.pos, 'R' if ant.dir == 1 else 'L')
            else:
                print('Fell off')
    print()