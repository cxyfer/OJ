from functools import cmp_to_key

n = int(input())
A = input().split()

def cmp(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1

A.sort(key=cmp_to_key(cmp))
print("".join(A))