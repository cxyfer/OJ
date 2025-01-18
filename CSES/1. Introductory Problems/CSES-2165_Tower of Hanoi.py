ans = []
def f(n, a, b, c): # n: number of disks, a: source, b: auxiliary, c: target
    if n == 1:
        print(a, c)
    else:
        f(n-1, a, c, b)
        print(a, c)
        f(n-1, b, a, c)
    
n = int(input())
print(pow(2, n) - 1)
f(n, 1, 2, 3)