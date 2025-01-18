from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

t = A[0] # B[1] ^ B[N]
for i in range(1, N-1):
    t ^= A[i]
ans = []
B = [0] * N
for i in range(N-1): # 枚舉第一個數字
    cnt = defaultdict(int)
    B[0] = i
    cnt[i] += 1
    flag = True
    for j in range(1, N):
        B[j] = A[j-1] ^ B[j-1]
        if B[j] >= N or B[j] < 0 or cnt[B[j]] > 0:
            flag = False
            break
        cnt[B[j]] += 1
    if B[0] ^ B[N-1] != t:
        flag = False
    if flag:
        print(*B, sep=' ')
        break


# print(max(cnt.values()))
# check = []
# for i in range(1, N):
#     check.append(B[i-1] ^ B[i])
# flag = True
# for i in range(N-1):
#     if check[i] != A[i]:
#         flag = False
#         break
# print('Yes' if flag else 'No')