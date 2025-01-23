from string import ascii_lowercase

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    if n - m > 26 or m == n:
        print("NO")
        continue

    if n <= 27:
        s = ascii_lowercase[:n-1] + ascii_lowercase[m-1]
    else:
        s = ascii_lowercase[:n-m] + ascii_lowercase * (m // 26 + 1)
        s = s[:n]

    print("YES")
    print(s)