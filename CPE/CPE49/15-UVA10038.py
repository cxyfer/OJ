while True:
    try:
        n, *nums = map(int, input().split())
    except EOFError:
        break
    flag = True
    cnt = [0] * (n)
    for i in range(n - 1):
        d = abs(nums[i] - nums[i + 1])
        if d < 1 or d >= n or cnt[d] > 0:
            flag = False
            break
        cnt[d] += 1
    print("Jolly" if flag else "Not jolly")
