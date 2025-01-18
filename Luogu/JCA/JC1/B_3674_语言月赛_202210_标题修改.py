s = list(input())
n = len(s)

i = j = 0
while i < n:
    if not s[i].isalpha():
        i += 1
        continue
    j = i
    while j < n and s[j].isalpha():
        if (j - i) & 1:
            s[j] = s[j].lower()
        else:
            s[j] = s[j].upper()
        j += 1
    i = j
print(''.join(s))
