N = int(input())
A = list(map(int, input().split()))

ans = set()
sums = []
def dfs(i, val):
    if i == N:
        ans.add(val)
        return
    
    sums.append(A[i])
    dfs(i + 1, val ^ A[i])
    sums.pop()

    for k in range(len(sums)):
        val ^= sums[k]
        sums[k] += A[i]
        val ^= sums[k]
        dfs(i + 1, val)
        val ^= sums[k]
        sums[k] -= A[i]
        val ^= sums[k]

dfs(0, 0)
print(len(ans))