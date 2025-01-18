from string import ascii_uppercase

keyboard = input()
ans = 0
cur = keyboard.index(ascii_uppercase[0])
for ch in ascii_uppercase:
    nxt = keyboard.index(ch)
    ans += abs(cur - nxt)
    cur = nxt
print(ans)