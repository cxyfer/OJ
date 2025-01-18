"""
    Selection Sort -> O(n^2) TLE
    Hash Table -> O(N)
"""
N = int(input())
A = list(map(int, input().split()))

mp = dict()
for i, a in enumerate(A):
    mp[a] = i

cnt = 0
ans = []
for i in range(N):
    if A[i] == i+1:
        continue
    cnt += 1
    idx = mp[i+1]
    A[i], A[idx] = A[idx], A[i]
    mp[A[idx]] = idx
    ans.append((i+1, idx+1))
print(cnt)
for a, b in ans:
    print(a, b)
