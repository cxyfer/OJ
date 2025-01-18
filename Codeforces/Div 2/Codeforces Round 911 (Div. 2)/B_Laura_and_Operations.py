T = int(input())

for tc in range(1, T+1):
    a, b, c = map(int, input().split())

    def check(a, b, c):
        if b % 2 == c % 2:
            return 1
        else:
            return 0
    
    print(check(a, b, c), check(b, c, a), check(c, a, b))
