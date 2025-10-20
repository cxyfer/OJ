mp = {"Ocelot": 0, "Serval": 1, "Lynx": 2}
x, y = map(lambda w: mp[w], input().split())
print("Yes" if x >= y else "No")
