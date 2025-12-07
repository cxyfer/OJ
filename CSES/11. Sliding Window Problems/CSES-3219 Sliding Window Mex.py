from heapq import heappush, heappop, heapify

def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    cnt = [0] * (k + 1)
    hp = list(range(k + 1))  # Mex
    heapify(hp)
    ans = []
    for r, x in enumerate(A):
        # 1. 入窗口
        if x <= k:
            cnt[x] += 1
        if r >= k - 1:
            # 2. 去除過期的堆頂元素
            while cnt[hp[0]] > 0:
                heappop(hp)
            # 3. 更新答案
            ans.append(hp[0])
            # 4. 出窗口
            y = A[r - k + 1]
            if y <= k:
                cnt[y] -= 1
                if cnt[y] == 0:
                    heappush(hp, y)
    print(*ans)

if __name__ == "__main__":
    solve()