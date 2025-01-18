t = int(input())
for tc in range(t):
    N = int(input())
    data = [list(map(int, input().split(" "))) for _ in range(N)]

    
    s0, e0 = data[0][0], data[0][1]
    ans = -1
    data = data[1:]
    for si, ei in data:
        if si >= s0 and ei >= e0: # 力量和耐力都比第一位運動員高
            ans = -1
            break
        elif si >= s0 and ei < e0: # 力量比第一位運動員高，但耐力比第一位運動員低
            continue
        elif si < s0 and ei >= e0: # 耐力比第一位運動員高，但力量比第一位運動員低
            ans = max(ans, si+1)
        else:
            ans = max(ans, si+1)
    print(ans)