"""
【虾皮】20250423_2_括号匹配（Bracket Validity）
https://niumacode.com/problem/P1594
"""

s = input()
st = []
for ch in s:
    if ch == '(':
        st.append(ch)
    elif ch == '[':
        if st and st[-1] == '(':
            exit(print('false'))
        st.append(ch)
    elif ch == ')':
        if st and st[-1] == '(':
            st.pop()
        else:
            exit(print('false'))
    elif ch == ']':
        if st and st[-1] == '[':
            st.pop()
        else:
            exit(print('false'))
print('true' if not st else 'false')