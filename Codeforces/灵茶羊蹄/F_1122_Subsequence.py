from bisect import bisect_left

n = int(input())
pos = [[] for _ in range(20)]

A = list(map(int, input().split()))
for i, v in enumerate(A):
    pos[v - 1].append(i)

# 令 f[i] 表示選擇已經選擇的數字集合為 i 時，最後一個數字的位置
f = [n] * (1 << 20)
f[0] = -1
ans = 0  # 最多能選擇的數字種類數
u = (1 << 20) - 1  # 宇集合
for i in range(1 << 20):
    if f[i] == n:
        continue
    ans = max(ans, i.bit_count())
    
    # 枚舉未選擇的數字，並嘗試添加
    j = u ^ i
    while j:
        lb = j & -j
        # 轉換為下標，lb == (1 << (lb.bit_length() - 1))
        ps = pos[lb.bit_length() - 1]

        # 連續擺兩個 lb 在 f[i] 之後
        idx1 = bisect_left(ps, f[i])
        idx2 = idx1 + 1
        if idx2 < len(ps):
            f[i | lb] = min(f[i | lb], ps[idx2])
        
        j ^= lb

print(ans * 2)