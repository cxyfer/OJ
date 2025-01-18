import heapq

t = int(input())

"""
    Editorial
"""
for tc in range(t):
    S = input()
    pos = int(input())
    n = tmp_len = len(S)
    cnt = 0 # 到目標位置pos，需要刪除幾次
    while (pos > tmp_len):
        pos -= tmp_len
        cnt += 1
        tmp_len -= 1
    st = [] # stack

    for i in range(n):
        while (st and cnt and S[i] < st[-1]):
            st.pop()
            cnt -= 1
        st.append(S[i])
    # print(st, pos)
    print(st[pos-1], end="")
