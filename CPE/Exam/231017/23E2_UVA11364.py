T = int(input())

for tc in range(1, T+1):
    n = int(input())
    X = list(map(int, input().split()))
    print((max(X) - min(X)) * 2)