from collections import defaultdict
from heapq import heappush, heappop

def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n
    
    ans = []
    cnt = defaultdict(int)
    hp = []  # (-cnt[x], x), Lazy Removal
    for r, x in enumerate(A):
        # 1. 入窗口
        cnt[x] += 1
        heappush(hp, (-cnt[x], x))
        if r >= k - 1:
            # 2. 去除過期的堆頂元素
            while cnt[hp[0][1]] != -hp[0][0]:  # 頻率不符，彈出
                heappop(hp)
            # 3. 更新答案
            ans.append(hp[0][1])
            # 4. 出窗口
            y = A[r - k + 1]
            cnt[y] -= 1
    print(*ans)

if __name__ == "__main__":
    solve()