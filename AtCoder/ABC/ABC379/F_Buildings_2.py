from atcoder.fenwicktree import FenwickTree

N, Q = map(int, input().split())
H = list(map(int, input().split()))
queries = []
for i in range(Q):
    l, r = map(int, input().split())
    queries.append((l, r, i))  # (l_i, r_i, query_id)

# 預處理每棟建築物的左側可見起點 L[j]，即 L[j], L[j+1], ... , j - 1 都比 H[j] 矮
st = []  # Monotonic Stack
L = [0] * N
for j, h in enumerate(H):
    while st and st[-1][1] <= h:
        st.pop()
    if st:
        L[j] = st[-1][0]
    else:
        L[j] = 0
    st.append((j + 1, h))

# 準備建築物列表 A，按照 L[j] 升序排序
A = sorted([(L[j], j + 1) for j in range(N)], key=lambda x: x[0])

bit = FenwickTree(N)
ans = [0] * Q
j = 0
for l_i, r_i, idx in sorted(queries, key=lambda x: x[0]):
    # 將所有 L[j] <= l_i 的建築物加入樹狀數組
    while j < N and A[j][0] <= l_i:
        bit.add(A[j][1] - 1, 1)
        j += 1
    # 計算能被同時從 l_i 和 r_i 觀察到的建築物數量
    ans[idx] = bit.sum(r_i, N)

print(*ans, sep='\n')  # 按照原始查詢順序輸出答案