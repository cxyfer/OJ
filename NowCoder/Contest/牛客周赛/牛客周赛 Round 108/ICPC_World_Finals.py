def solve():
    a, *s = map(int, input().split())
    if a < 425 and any(x < 60 for x in s):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()