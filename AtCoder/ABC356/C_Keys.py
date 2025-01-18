"""
    N <= 15
"""
N, M, K = map(int, input().split())

tests = []
results = []
for _ in range(M):
    c, *keys, r = input().split()
    state = 0 # 狀態壓縮
    for key in map(int, keys):
        state |= 1 << (key - 1)
    tests.append(state)
    results.append(True if r == "o" else False)

ans = 0
for i in range(1 << N): # N <= 15
    for j in range(M):
        if ((i & tests[j]).bit_count() >= K) != results[j]: # 與測試結果不符
            break
    else:
        ans += 1
print(ans)