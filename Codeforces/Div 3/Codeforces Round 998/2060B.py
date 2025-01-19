t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    cows = [sorted(map(int, input().split())) for _ in range(n)]
    
    cards = []
    for idx, cow in enumerate(cows):
        for val in cow:
            cards.append((val, idx))
    cards.sort(key=lambda x: x[0])
  
    ans = [-1] * n
    rounds = [[] for _ in range(n)]
    for i, (val, idx) in enumerate(cards):
        rounds[idx].append(i)
        
    if any(len(r) != m for r in rounds):
        print(-1)
        continue
    
    for i, round in enumerate(rounds):
        if any(round[j] - round[j-1] != n for j in range(1, m)):
            print(-1)
            break
        else:
            ans[round[0]] = i + 1
    else:
        print(*ans)