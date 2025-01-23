MOD = int(1e9 + 7)

MX = 10
fact = [1] * MX
invf = [1] * MX
for i in range(1, MX):
    fact[i] = fact[i - 1] * i % MOD
invf[MX - 1] = pow(fact[MX - 1], MOD - 2, MOD)
for i in range(MX - 2, -1, -1):
    invf[i] = invf[i + 1] * (i + 1) % MOD

def comb(n: int, m: int) -> int:
    return fact[n] * invf[m] * invf[n - m] % MOD

def solve():
    n = int(input())
    grid = [input() for _ in range(3)]
    
    # 紀錄 mod 3 後為 0, 1, 2 的 column 有哪些數字
    vis = [set() for _ in range(3)]
    for i in range(3):
        for j in range(n):
            if grid[i][j] == '?':
                continue
            vis[j % 3].add(grid[i][j])
    
    # 1. More than 3 numbers in a column
    if any(len(x) > 3 for x in vis):
        print("0")
        return
    
    # 2. Same number in different columns
    if vis[0] & vis[1] or vis[0] & vis[2] or vis[1] & vis[2]:
        print("0")
        return
    
    # 3. Duplicate numbers in same column
    for j in range(n):
        if grid[0][j] != '?' and grid[0][j] == grid[1][j] \
        or grid[0][j] != '?' and grid[0][j] == grid[2][j] \
        or grid[1][j] != '?' and grid[1][j] == grid[2][j]:
            print("0")
            return
    
    # Count question marks in each column
    cnt = [sum(grid[j][i] == '?' for j in range(3)) for i in range(n)]
    
    # Number allocation
    cols = [3 - len(vis[j]) for j in range(3)]  # mod 3 後為 0, 1, 2 的 column 需要的數字數量
    tot = sum(cols)  # 總共需要的數字數量
    
    # 將 cols[0] 個數字分配給第一個 column、cols[1] 個數字分配給第二個 column、cols[2] 個數字分配給第三個 column
    ans = comb(tot, cols[0]) * comb(tot - cols[0], cols[1]) % MOD
    for i in range(n):
        ans = ans * fact[cnt[i]] % MOD
    print(ans)

t = int(input())

for _ in range(t):
    solve()