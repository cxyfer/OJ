
s = input()
target = "aeiou"
for ch in s:
    if ch not in target:
        print(ch, end="")