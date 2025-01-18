n = int(input())

def gray_code(n):
    if n == 0:
        return [0]
    prev = gray_code(n - 1)
    return prev + [2 ** (n - 1) + x for x in prev[::-1]]

for x in gray_code(n):
    print(bin(x)[2:].zfill(n))