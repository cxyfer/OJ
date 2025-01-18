N, M = map(int, input().split())
S = input()
T = input()

X = "#" * N

S = S.replace(T, "#"*M)
flag = True # 有更新可以檢查
while(flag):
    
    flag = False
    # 枚舉起點
    i = 0
    while i < N-M+1: 
        if S[i:i+M] == "#" * M:
            i += 1
            continue
        # 檢查是否可以匹配
        match = True
        for j in range(M):
            if S[i+j] != "#" and S[i+j] != T[j]:
                match = False
                break
        if match:
            flag = True
            S = S[:i] + "#" * M + S[i+M:]
            i += M
        else:
            i += 1
print("Yes" if S.count("#") == N else "No")
 