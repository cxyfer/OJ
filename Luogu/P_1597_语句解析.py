s = input().strip().split(";")
s = [x.split(":=") for x in s if x]

ans = [0] * 3
for x, y in s:
    ans[ord(x) - ord("a")] = int(y) if y.isdigit() else ans[ord(y) - ord("a")]
print(*ans)