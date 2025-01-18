a = int(input())
b = int(input())
c = int(input())

ans = [a] * 50 + [b] * 45 + [c] * 4 + [c + 1]
print(100)
print(*ans)