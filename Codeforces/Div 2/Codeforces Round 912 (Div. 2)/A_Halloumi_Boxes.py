# 沒看到最多 = =
# 只要 K = 2 時就一定可以
# K = 1 時，如果 A 是升序，也可以

T = int(input())

def check(A): # A是否為升序
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    flag = check(A)
    if flag or K >= 2:
        print("YES")
        continue
    else:
        print("NO")
        continue
    
    