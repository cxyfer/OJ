"""
    Stack

    tags: AOAPC-BAC-Ch6
"""
N = int(input())

mp = dict()
for _ in range(N):
    ch, m, n = input().split()
    mp[ch] = (int(m), int(n))

while True:
    try:
        line = input()
    except EOFError:
        break
    ans = 0
    st = []
    for ch in line:
        if ch in mp.keys():
            st.append(mp[ch])
        elif ch == "(":
            # st.append("(")
            pass
        elif ch == ")":
            x2, y2 = st.pop()
            x1, y1 = st.pop()
            if y1 != x2:
                ans = -1
                break
            ans += x1 * y1 * y2
            # st.pop() # pop "("
            st.append((x1, y2))  # new matrix size
    print(ans if ans != -1 else "error")