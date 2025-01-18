"""
    由於每個字元都不同，且最後至少存留一個字元，所以可以這樣貪
"""
s = input()
n = len(s)
x = y = 0
s += "$$$"
for i in range(n):
    if s[i] == 'b' or s[i + 1] == 'o' or s[i + 2] == 'y':
        x += 1
    if s[i] == 'g' or s[i + 1] == 'i' or s[i + 2] == 'r' or s[i + 3] == 'l':
        y += 1
print(x, y, sep="\n")