from collections import Counter

s = input()
cnt = Counter(s)
print(''.join(ch for ch, v in cnt.items() if v == 1))
