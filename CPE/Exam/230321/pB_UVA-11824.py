t = int(input())

for _ in range(t):
    arr = []
    x = int(input())
    while x:
        arr.append(x)
        x = int(input())
    arr.sort(reverse=True)
    cost = 0
    for i, x in enumerate(arr):
        cost += 2 * x ** (i+1)
    print(cost if cost <= 5e6 else "Too expensive")