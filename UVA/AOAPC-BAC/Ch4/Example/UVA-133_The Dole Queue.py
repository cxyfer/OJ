""" UVA-133 The Dole Queue
    看起來很複雜，但數據範圍很小，直接模擬即可
    tags: 模擬, 紫書-Ch4,
"""

def nxt(p, dir, step):
    while step:
        p = (p + dir + n) % n
        if not visited[p]:
            step -= 1
    return p

while True:
    n, k, m = map(int, input().split())
    if n == 0 and k == 0 and m == 0:
        break
    visited = [False] * n
    left, right = -1, n
    cnt = 0
    while cnt < n:
        left = nxt(left, 1, k)
        right = nxt(right, -1, m)
        visited[left] = visited[right] = True
        if left == right:
            print(f"{left+1:3d}", end="," if cnt < n - 1 else "\n")
            cnt += 1
        else:
            print(f"{left+1:3d}{right+1:3d}", end="," if cnt < n - 2 else "\n")
            cnt += 2



