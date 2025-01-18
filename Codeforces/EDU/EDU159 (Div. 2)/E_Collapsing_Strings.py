from collections import Counter

N = int(input())
strs = [input() for _ in range(N)]

prefix = Counter()
suffix = Counter()

for s in strs:
    for j in range(1, len(s)+1):
        # print(s[:j])
        prefix[s[:j]] += 1
    for j in range(len(s)-1, -1, -1):
        # print(s[j:])
        suffix[s[j:]] += 1

NN = sum([len(s) for s in strs])
ans = NN * (N*2)
for s in strs:
    for j in range(1, len(s)+1):
        # print(s[:j])
        ans -= suffix[s[:j][::-1]]
    for j in range(len(s)-1, -1, -1):
        # print(s[j:])
        ans -= prefix[s[j:][::-1]]

print(ans)
