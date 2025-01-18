from collections import Counter

tc = 1
while True:
    try:
        line = input()
        while not line:
            line = input()
        n = int(line)
        arr = list(map(int, input().split()))
    except EOFError:
        break
    flag = True if arr[0] >= 1 else False
    for i in range(n-1):
        if arr[i] >= arr[i+1]:
            flag = False
            break

    cnt = Counter()
    for i in range(n):
        for j in range(i, n):
            if cnt[arr[i] + arr[j]] > 0:
                flag = False
                break
            cnt[arr[i] + arr[j]] += 1
    print(f"Case #{tc}: It is ", end="")
    print("not a B2-Sequence." if not flag else "a B2-Sequence.", end="\n\n")
    tc += 1