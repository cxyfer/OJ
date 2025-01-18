""" UVA 10056 - What is the Probability?
    # Math
    首項為 (1-P)^(I-1) * P ，公比為 (1-P)^N 的無窮等比級數和
"""
T = int(input())

for _ in range(T):
    ins = input().split()
    N = int(ins[0])
    P = float(ins[1])
    I = int(ins[2])
    if P == 0:
        ans = 0
    else:
        ans = (1 - P) ** (I - 1) * P / (1 - (1 - P) ** N)
    print("{:.4f}".format(ans))