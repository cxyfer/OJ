from collections import Counter

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    S = input()

    ans = 0
    cnt = Counter(S)
    mx = cnt.most_common(1)[0][1] # most common character's frequency
    
    if mx > N - mx:
        print(2 * mx - N)
    else:
        print(N % 2)