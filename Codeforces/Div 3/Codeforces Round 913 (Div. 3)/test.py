def min_length(s):
    st1 = []
    for ch in s:
        if st1 and st1[-1] == ch:
            st1.pop()
            st1.append(ch)
        else:
            st1.append(ch)
    st2 = []
    for ch in st1:
        if st2 and st2[-1] != ch:
            st2.pop()
        else:
            st2.append(ch)
    print(st2)
    return len(st2)

print(min_length("dabbb"))