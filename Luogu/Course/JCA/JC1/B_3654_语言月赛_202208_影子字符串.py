ans = ""
st = set()

while True:
    s = input()
    if s == "0":
        break
    if s not in st:
        st.add(s)
        ans += s

print(ans)