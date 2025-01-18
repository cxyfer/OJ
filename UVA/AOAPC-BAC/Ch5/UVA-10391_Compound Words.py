words = []
st = set()

while True:
    try:
        s = input()
        words.append(s)
        st.add(s)
    except EOFError:
        break

for word in words:
    for i in range(1, len(word)):
        if word[:i] in st and word[i:] in st:
            print(word)
            break