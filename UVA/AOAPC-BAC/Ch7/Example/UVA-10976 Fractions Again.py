"""
1/k = 1/x + 1/y, x >= y

1. 1/k - 1/y = 1/x
=> (y - k) / ky = 1/x
=> x = ky / (y - k) 
=> y > k

2. x >= y
=> 1/y >= 1/x
=> 1/y >= 1/k - 1/y
=> 2/y >= 1/k
=> y <= 2k
"""

while True:
    try:
        k = int(input().strip())
    except EOFError:
        break

    ans = []
    for y in range(k + 1, 2 * k + 1): # k < y <= 2k
        num = y * k
        den = y - k
        if num % den != 0:
            continue
        x = num // den
        if x >= y:
            ans.append((x, y))
    print(len(ans))
    for x, y in ans:
        print(f"1/{k} = 1/{x} + 1/{y}")