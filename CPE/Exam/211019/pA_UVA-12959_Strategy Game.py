while True:
    try:
        N, R = map(int, input().split())
    except:
        break
    A = list(map(int, input().split()))
    scores = [0] * N
    for i in range(R):
        for j in range(N):
            scores[j] += A[i * N + j]
    ans = max(range(N), key=lambda x: (scores[x], x))
    print(ans + 1)