while True:
    x, y = map(int, input().split())
    if x == y == 0:
        break
    ans = 0
    carry = 0
    while x or y:
        if x % 10 + y % 10 + carry > 9:
            ans += 1
            carry = 1
        else:
            carry = 0
        x //= 10
        y //= 10
    print((str(ans) if ans else "No") + " carry operation" + ("s." if ans > 1 else "."))
