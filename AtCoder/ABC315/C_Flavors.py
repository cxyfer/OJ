# Input & Pre-processing:
N = int(input())
flavors = []
dic = {i:[] for i in range(1, N + 1) }

for _ in range(N):
    f, d = map(int, input().split())
    dic[f].append(d)
    flavors.append((f, d)) 
flavors.sort(key=lambda x: x[1], reverse=True)

ans = 0
# Same flavor
for f in range(1, N + 1):
    if len(dic[f]) >= 2:
        dic[f].sort(reverse=True)
        ans = max(ans, dic[f][0] + dic[f][1] // 2)
# Diff flavor
for f, d in flavors[1:]:
    if f != flavors[0][0]:
        ans = max(ans, flavors[0][1] + d)
        break
print(ans)

