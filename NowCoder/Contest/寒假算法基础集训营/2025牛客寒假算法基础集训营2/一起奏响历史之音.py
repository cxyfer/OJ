A = list(map(int, input().split()))

print("YES" if all(x != 4 and x != 7 for x in A) else "NO")