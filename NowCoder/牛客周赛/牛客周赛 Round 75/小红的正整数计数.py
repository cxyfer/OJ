L, R = map(int, input().split())

def cal(x):
    return x // 2

print(cal(R) - cal(L - 1))