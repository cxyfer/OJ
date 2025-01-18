from collections import Counter
import string

while True:
    try:
        a = input()
        b = input()
    except EOFError:
        break
    
    cnt_a = Counter(a)
    cnt_b = Counter(b)

    ans = ""
    for ch in string.ascii_lowercase:
        ans += ch * min(cnt_a[ch], cnt_b[ch])
    print(ans)