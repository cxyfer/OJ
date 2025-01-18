"""
    Stack
"""

S = input()

st = []
for ch in S:
    if len(st) >= 2 and st[-2] == 'A' and st[-1] == 'B' and ch == 'C':
        st.pop()
        st.pop()
    else:
        st.append(ch)
print(''.join(st))