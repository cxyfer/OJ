t = int(input())

def solve(n):
    for x in range(1, n):
        for y in range(x+1, n-x):
            z = n - (x + y)
            if (z == x or z == y):
                continue
            if (x % 3 == 0 or y % 3 == 0 or z % 3 == 0):
                continue
            print("YES")
            print(x, y, z)
            return
    print("NO")

for i in range(t):
    n = int(input())
    solve(n)
    


