from collections import deque

MAX = int(1e5 + 5)

N = int(input())
A = list(map(int, input().split()))

# Counting Sort
cnt = [0] * MAX
for a in A:
    cnt[a] += 1
B = []
for x in range(MAX):
    if cnt[x] > 0:
        B.extend([x] * cnt[x])

ans = 0
q1, q2 = deque(B), deque()
def pop():
    if len(q2) == 0:
        return q1.popleft()
    elif len(q1) == 0:
        return q2.popleft()
    else:
        return q1.popleft() if q1[0] < q2[0] else q2.popleft()

while len(q1) + len(q2) > 1:
    x, y = pop(), pop()
    ans += x + y
    q2.append(x + y)
print(ans)