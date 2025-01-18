from collections import deque, defaultdict

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = list(input())
    A = list(map(int, input().split()))
    que = [set() for _ in range(N)]
    for i in range(N):
        A[i] -= 1
        que[A[i]].add(i)
    ts = deque()
    for i in range(N):
        if len(que[i]) == 0:
            ts.append(i)
    drr = []
    while ts:
        len_ = len(ts)
        for _ in range(len_):
            k = ts.popleft()
            if S[k] == '1':
                S[k] = str(int(S[k]) ^ 1)
                S[A[k]] = str(int(S[A[k]]) ^ 1)
                drr.append(k)
            que[A[k]].discard(k)
            if len(que[A[k]]) == 0:
                ts.append(A[k])
    tmp = False
    for i in range(N):
        if S[i] == '1':
            da = {}
            crr = []
            cnt = 0
            wei = i
            while True:
                if wei not in da:
                    da[wei] = 1
                else:
                    break
                cnt += 1
                if S[wei] == '1':
                    crr.append(cnt)
                wei = A[wei]
            len_ = len(crr)
            if len_ % 2 == 1:
                tmp = True
                break
            else:
                zhi1 = 0
                zhi2 = 0
                for j in range(1, len_, 2):
                    zhi1 += crr[j] - crr[j-1]
                zhi2 += crr[0] + cnt - crr[len_-1]
                for j in range(2, len_-1, 2):
                    zhi2 += crr[j] - crr[j-1]
                da.clear()
                wei = A[i]
                if zhi1 <= zhi2:
                    wei = i
                shang = 0
                while True:
                    if wei not in da:
                        da[wei] = 1
                        if S[wei] == '1':
                            S[wei] = str(int(S[wei]) ^ 1)
                            shang ^= 1
                    else:
                        break
                    if shang == 1:
                        drr.append(wei)
                    wei = A[wei]
    if tmp:
        print(-1)
    else:
        print(len(drr))
        for x in drr:
            print(x+1, end=' ')
        print()