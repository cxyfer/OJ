from collections import deque


def solve():
    n, k, d = map(int, input().split())
    A = list(map(int, input().split()))

    # 滑動窗口最大值/最小值
    ans = -1
    q_mx = deque()
    q_mn = deque()
    left = 0
    for i, x in enumerate(A):
        # 1. 入窗口
        while q_mx and A[q_mx[-1]] < x:
            q_mx.pop()
        q_mx.append(i)
        while q_mn and A[q_mn[-1]] > x:
            q_mn.pop()
        q_mn.append(i)

        # 2. 差值太大，需要出窗口
        while A[q_mx[0]] - A[q_mn[0]] > d:
            if q_mx[0] < q_mn[0]:
                left = q_mx.popleft() + 1
            else:
                left = q_mn.popleft() + 1

        # 3. 更新答案
        if i - left + 1 >= k:
            ans = max(ans, i - left + 1)
    print(ans)


if __name__ == "__main__":
    solve()
