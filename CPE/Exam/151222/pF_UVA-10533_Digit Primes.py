"""
    埃氏篩 + 前綴和
"""
import sys
input = sys.stdin.readline
def print(val=""): sys.stdout.write(str(val) + "\n")

MAX_N = int(1e6 + 5)

is_prime = [True] * MAX_N
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX_N ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N, i):
            is_prime[j] = False

def digit_sum(n: int) -> int:
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res

s = [0] * MAX_N
for i in range(2, MAX_N):
    if is_prime[i] and is_prime[digit_sum(i)]:
        s[i] = s[i - 1] + 1
    else:
        s[i] = s[i - 1]

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    print(s[r] - s[l - 1])