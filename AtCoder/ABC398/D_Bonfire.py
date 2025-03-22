N, R, C = map(int, input().split())
S = input()
DIR = {"N": (-1, 0), "W": (0, -1), "S": (1, 0), "E": (0, 1)}

st = set([(0, 0)])
sx = sy = 0
ans = [''] * N
for i, d in enumerate(S):
    dx, dy = DIR[d]
    sx += dx
    sy += dy
    ans[i] = '1' if (sx - R, sy - C) in st else '0'
    st.add((sx, sy))
print(''.join(ans))