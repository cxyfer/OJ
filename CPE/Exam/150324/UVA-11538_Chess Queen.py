def perm2(n): # perm(n, 2)
    return n * (n - 1)

while True:
    n, m = map(int, input().strip().split())
    if n == 0 and m == 0:
        break
    if n > m:
        n, m = m, n
    ans = 0
    ans += m * perm2(n)
    ans += n * perm2(m)
    """
    有 m - n + 1 個左斜線長度為 n，有 2 * (n - 1) 條分別為 n - 1, n - 2, ..., 1
    
    sum_{i=1}^{n-1} perm(i, 2) = sum_{i=1}^{n-1} i * (i - 1)
    = sum_{i=1}^{n-1} i^2 - i
    = (n - 1) * n * (2 * n - 1) / 6 - (n - 1) * n / 2
    = n * (n - 1) * (n - 2) / 3
    """
    slash = (m - n + 1) * perm2(n) + 2 * ((n - 1) * n * (n - 2)) // 3 
    ans += 2 * slash
    print(ans)
